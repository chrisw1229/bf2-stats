(function($, undefined) {

$.widget('ui.table', {

   // Configure the default widget options
   options: {
      columns: [],
      maxRows: 10,
      showAll: false,
      sortIndex: -1,
      sortAsc: undefined
   },

   _create: function() {

      this.columns = [];
      this.rows = [];
      this.sortIndex = this.options.sortIndex;
      this.sortAsc = this.options.sortAsc;

      // Build the document model
      this.element.addClass('ui-table');

      // Create the main table element
      this.tableElm = $('<table class="ui-table-container"/>').appendTo(this.element);
      this.bodyElm = $('<tbody class="ui-table-body"/>').appendTo(this.tableElm);
      this.headerElm = $('<tr class="ui-table-header"/>').appendTo(this.bodyElm);
      this.footerElm = $('<tr class="ui-table-footer"><td class="ui-state-default ui-corner-bottom" colspan="0">&nbsp;</td></tr>').appendTo(this.bodyElm);

      var footerCell = $('td', this.footerElm);
      this.showMoreElm = $('<a class="ui-table-show ui-table-show-more">'
            + '<span class="ui-icon ui-icon-triangle-1-s"/>'
            + '<span>Show more</span></a>').appendTo(footerCell);
      this.showLessElm = $('<a class="ui-table-show ui-table-show-less">'
            + '<span class="ui-icon ui-icon-triangle-1-n"/>'
            + '<span>Show less</span></a>').appendTo(footerCell);

      // Create the status message rows
      this.emptyElm = $('<tr class="ui-state-active ui-table-empty"><td colspan="0"><span class="ui-icon ui-icon-alert"/>No Records Available</td></tr>');
      this.loadElm = $('<tr class="ui-state-active ui-table-load"><td colspan="0"><span class="ui-icon"/>Loading...</td></tr>');
      this.errorElm = $('<tr class="ui-state-error ui-table-error"><td colspan="0"><span class="ui-icon ui-icon-alert"/>ERROR - Records Not Found</td></tr>');

      // Bind event handlers for the table header cells
      this.headerElm.on('mouseenter', '.ui-table-header',
            function(e) { $(this).addClass('ui-state-hover'); });
      this.headerElm.on('mouseleave', 'th',
            function(e) { $(this).removeClass('ui-state-hover'); });
      this.headerElm.on('click', 'th', $.proxy(this._onSortClick, this));
 
      // Bind event handlers for the footer cells
      this.showMoreElm.on('click', $.proxy(this._onShowMoreClick, this));
      this.showLessElm.on('click', $.proxy(this._onShowLessClick, this));

      // Initialize the table columns
      this.setColumns(this.options.columns);
   },

   destroy: function() {

      // Clear the event handlers
      this.showMoreElm.off('click');
      this.showLessElm.off('click');
      this.headerElm.off('mouseenter mouseleave click');

      // Destroy the document model
      this.tableElm.remove();
      this.element.removeClass('ui-table');

      $.Widget.prototype.destroy.call(this);
   },

   setColumns: function(columns) {

      // Reset the table to clear previous columns and rows
      this.reset();

      // Make sure there are columns to display
      if (columns == undefined || columns.length <= 0) {
         return;
      }

      // Create a column element to store the row number
      this.headerElm.empty();
      $('<th class="ui-state-default ui-corner-tl ui-table-cell-rank">#</th>').appendTo(this.headerElm);

      // Add the new table column header elements
      var sortIndex = undefined, sortAsc = undefined;
      for (var i = 0; i < columns.length; i++) {

         // Store the column data for future use
         var column = columns[i];
         this.columns.push(column);

         // Check if this is the default sort column
         sortIndex = (column.sorted != undefined ? i : sortIndex);
         sortAsc = (column.sorted != undefined ? column.sorted : sortAsc);

         // Create an element to represent the column header
         var columnElm = $('<th class="ui-state-default ui-table-header' 
               + (i == columns.length - 1 ? ' ui-corner-tr ' : '')
               + '"/>').appendTo(this.headerElm);
         $('<span class="">' + column.name + '</span>').appendTo(columnElm);
         $('<span class="ui-icon ui-table-sort-icon"/>').appendTo(columnElm);
      }

      // Align the various message and footer row elements
      this.emptyElm.children(':first').attr('colspan', columns.length + 1);
      this.loadElm.children(':first').attr('colspan', columns.length + 1);
      this.errorElm.children(':first').attr('colspan', columns.length + 1);
      this.footerElm.children(':first').attr('colspan', columns.length + 1);

      // Update the default sort if applicable
      this.setSort(sortIndex, sortAsc);
   },

   setRows: function(rows) {
      rows = ($.isArray(rows) ? rows : [rows]);

      // Clear the current table data
      this.clear();

      // Add all the new rows to the model
      this.rows = this.rows.concat(rows);

      // Sort the rows based on the current sort column
      this._sort();

      // Determine the current number of rows to create
      var maxRows = this.rows.length;
      if (!this.options.showAll) {
         maxRows = Math.min(this.rows.length, this.options.maxRows);
      }

      // Create table elements for each row of values
      for (var i = 0; i < maxRows; i++) {
         this._createRow(i);
      }

      // Update the footer actions
      if (this.options.showAll) {
         this.showMoreElm.hide();
         this.showLessElm.show();
      } else {
         if (this.rows.length > this.options.maxRows) {
            this.showMoreElm.show();
         }
         this.showLessElm.hide();
      }

      // Fill the table elements with row values
      this._display();
   },

   setSort: function(index, asc) {

      // Check whether the sort actually changed
      if (this.sortIndex == index && this.sortAsc == asc) {
         return;
      }

      // Set the sort direction based on the input
      if (this.sortIndex == index) {
         this.sortAsc = (asc != undefined ? asc : !this.sortAsc);
         this.rows.reverse();
      } else {
         this.sortIndex = index;
         this.sortAsc = (asc != undefined ? asc : true);
         this._sort();
      }

      // Update the sort direction icon
      $('.ui-table-header-sorted', this.headerElm).removeClass(
            'ui-table-header-sorted');
      $('.ui-table-header', this.headerElm).eq(this.sortIndex).addClass(
            'ui-table-header-sorted');
      $('.ui-table-sort-icon', this.headerElm).attr('class',
            'ui-icon ui-icon-triangle-1-' + (this.sortAsc ? 'n' : 's')
            + ' ui-table-sort-icon');

      // Fill the table elements with row values
      this._display();
   },

   clear: function() {
      this.rows = [];
      $('.ui-table-row', this.bodyElm).remove();

      // Display the empty table message
      this.loadElm.remove();
      this.errorElm.remove();
      this.emptyElm.insertBefore(this.footerElm);

      // Hide the footer actions
      this.showMoreElm.hide();
      this.showLessElm.hide();
   },

   reset: function() {

      // Clear the current table data
      this.clear();

      // Cleanup any previous table columns
      this.columns = [];
      this.sortIndex = undefined;
      this.sortAsc = undefined;
      this.headerElm.empty();

      // Add a default column to display
      $('<th class="ui-state-default ui-corner-top ui-table-cell-empty">&nbsp;</th>').appendTo(this.headerElm);
   },

   loading: function() {
      this.reset();
      this.emptyElm.remove();
      this.errorElm.remove();
      this.loadElm.insertBefore(this.footerElm);
   },

   error: function() {
      this.reset();
      this.emptyElm.remove();
      this.loadElm.remove();
      this.errorElm.insertBefore(this.footerElm);
   },

   _sort: function() {
      var columns = this.columns;
      var index = this.sortIndex;
      var asc = this.sortAsc;

      // Check if the sort index is valid
      if (index != undefined && index >= 0 && index < this.rows.length) {

         // Use the standard sort function with custom comparator
         this.rows.sort(function(row1, row2) {

            // Make sure string comparisons are case-insensitive
            var column = columns[index];
            var val1 = row1[index];
            var val2 = row2[index];

            val1 = (column.data == 'string' ? val1.toLowerCase() : val1);
            val2 = (column.data == 'string' ? val2.toLowerCase() : val2);

            // Adjust the result based on the sort direction
            if (val1 < val2) {
               return (asc ? -1 : 1);
            } else if (val1 > val2) {
               return (asc ? 1 : -1);
            }
            return 0;
         });
      }
   },

   _display: function() {

      // Check if the table contains row data
      if (this.rows.length == 0) {
         return;
      }

      // Remove the loading and empty table messages
      this.emptyElm.remove();
      this.loadElm.remove();

      // Fill in each row of values
      var rowElms = this.bodyElm.children();
      for (var i = 1; i < rowElms.length - 1; i++) {
         var cellElms = $(rowElms[i]).children();

         // Fill in each cell of values
         var r = i - 1;
         for (var j = 1; j < cellElms.length; j++) {
            var c = j - 1;

            // Check if there is a value defined for the cell
            if (r < this.rows.length && c < this.rows[r].length) {
               $(cellElms[j]).text(this.rows[r][c]);
            } else {
               $(cellElms[j]).text('');
            }
         }
      }
   },

   _createRow: function(index) {

      // Create a new table row to store the data
      var sequence = (index % 2 == 0 ? 'even' : 'odd');
      var rowElm = $('<tr class="ui-table-row ui-table-row-'
            + sequence + '"/>').insertBefore(this.footerElm);

      // Create a cell to display the row number
      $('<td class="ui-table-cell ui-table-cell-rank">'
            + (index + 1) + '</td>').appendTo(rowElm);

      // Add all the values as cells to the table row
      for (var i = 0; i < this.columns.length; i++) {
         var column = this.columns[i];
         $('<td class="ui-table-cell'
               + (column.data ? ' ui-table-data-' + column.data : '')
               + '"/>').appendTo(rowElm);
      }
   },

   _onSortClick: function(e) {
      var cellElm = $(e.target).closest('th');
      this.setSort(cellElm.index() - 1, !this.sortAsc);
   },

   _onShowMoreClick: function(e) {
      if (this.options.showAll) {
         return;
      }
      this.options.showAll = true;

      // Update the table footer actions
      this.showMoreElm.hide();
      this.showLessElm.show();

      // Create table elements for the remaining hidden rows
      for (var i = this.bodyElm.children().length - 2; i < this.rows.length; i++) {
         this._createRow(i);
      }

      // Fill the table elements with row values
      this._display();
   },
   
   _onShowLessClick: function(e) {
      if (!this.options.showAll) {
         return;
      }
      this.options.showAll = false;

      // Update the table footer actions
      this.showMoreElm.show();
      this.showLessElm.hide();

      // Destroy table elements for the extra displayed rows
      var rowElms = this.bodyElm.children();
      var startIndex = Math.min(this.rows.length, this.options.maxRows) + 1;
      var endIndex = rowElms.length - 1;
      rowElms.slice(startIndex, endIndex).remove();
   }

});

}(jQuery));
