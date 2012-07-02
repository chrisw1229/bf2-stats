(function($, undefined) {

$.widget('ui.table', {

   // Configure the default widget options
   options: {
      columns: [],
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

      // Create the status message rows
      this.emptyElm = $('<tr class="ui-state-active ui-table-empty"><td colspan="0">No Records Available</td></tr>');
      this.loadElm = $('<tr class="ui-state-active ui-table-load"><td colspan="0"><span class="ui-icon"/>Loading...</td></tr>');
      this.errorElm = $('<tr class="ui-state-error ui-table-error"><td colspan="0"><span class="ui-icon ui-icon-alert"/>ERROR - Records Not Found</td></tr>');

      this.headerElm.on('mouseenter', '.ui-table-header',
            function(e) { $(this).addClass('ui-state-hover'); });
      this.headerElm.on('mouseleave', 'th',
            function(e) { $(this).removeClass('ui-state-hover'); });
      this.headerElm.on('click', 'th',
            function(e) { self.setSort(e.data.index); });
 
      // Initialize the table columns
      this.setColumns(this.options.columns);
   },

   destroy: function() {

      // Clear the event handlers
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
               + '">' + column.name + '</th>').appendTo(this.headerElm);
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

      // Create table elements for each row of values
      for (var i = 0; i < this.rows.length; i++) {
         this._createRow(i);
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
   },

   reset: function() {

      // Clear the current table data
      this.clear();

      // Cleanup any previous table columns
      this.columns = [];
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
      var index = this.sortIndex;
      var asc = this.sortAsc;

      // Check if the sort index is valid
      if (index != undefined && index >= 0 && index < this.rows.length) {

         // Use the standard sort function with custom comparator
         this.rows.sort(function(row1, row2) {

            // Make sure string comparisons are case-insensitive
            var val1 = row1[index];
            var val2 = row2[index];
            val1 = (typeof(val1) == 'string' ? val1.toLowerCase() : val1);
            val2 = (typeof(val2) == 'string' ? val2.toLowerCase() : val2);

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
         $('<td class="ui-table-cell"/>').appendTo(rowElm);
      }
   }

});

}(jQuery));
