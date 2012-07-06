(function($, undefined) {

$.widget('ui.list', {

   // Configure the default widget options
   options: {
      builder: undefined
   },

   _create: function() {

      // Build the document model
      this.element.addClass('ui-list');
      this.listElm = $('<ol class="ui-list-items"/>').appendTo(this.element);

      // Create the status message rows
      this.emptyElm = $('<div class="ui-state-active ui-list-empty"><span class="ui-icon ui-icon-alert"/>No Records Available</div>');
      this.loadElm = $('<div class="ui-state-active ui-list-load"><span class="ui-icon"/>Loading...</div>');
      this.errorElm = $('<div class="ui-state-error ui-list-error"><span class="ui-icon ui-icon-alert"/>ERROR - Records Not Found</div>');

      // Bind event handlers for the list items
      this.listElm.on('mouseenter', '.ui-list-row',
            function(e) { $(this).addClass('ui-state-hover'); });
      this.listElm.on('mouseleave', '.ui-list-row',
            function(e) { $(this).removeClass('ui-state-hover'); });
   },

   destroy: function() {

      // Destroy the document model
      this.emptyElm.remove();
      this.loadElm.remove();
      this.errorElm.remove();
      this.listElm.remove();
      this.element.removeClass('ui-list');

      $.Widget.prototype.destroy.call(this);
   },

   setRows: function(rows) {
      rows = ($.isArray(rows) ? rows : [rows]);

      // Clear the current list data
      this.clear();

      // Add all the new rows to the model
      this.rows = this.rows.concat(rows);

      // Fill the list elements with row values
      for (var i = 0; i < this.rows.length; i++) {
         var item = this.rows[i];
         if (item) {
            this._displayRow(i, item);
         }
      }

      // Remove the loading and empty list messages
      if (rows.length > 0) {
         this.emptyElm.remove();
         this.loadElm.remove();
      }
   },

   clear: function() {
      this.rows = [];
      $('.ui-list-row', this.bodyElm).remove();

      // Display the empty list message
      this.loadElm.remove();
      this.errorElm.remove();
      this.emptyElm.appendTo(this.element);
   },

   loading: function() {
      this.clear();
      this.emptyElm.remove();
      this.errorElm.remove();
      this.loadElm.appendTo(this.element);
   },

   error: function() {
      this.clear();
      this.emptyElm.remove();
      this.loadElm.remove();
      this.errorElm.appendTo(this.element);
   },

   _displayRow: function(index, item) {

      // Create a new list row to store the data
      var sequence = (index % 2 == 0 ? 'even' : 'odd');
      var rowElm = $('<li class="ui-widget ui-state-default'
            + ' ui-list-row ui-list-row-' + sequence
            + (index == 0 ? ' ui-corner-top' : '')
            + (index == this.rows.length - 1 ? ' ui-corner-bottom' : '')
            + '"/>').appendTo(this.listElm);

      // Check whether a custom list item builder was provided
      var contentElm;
      if ($.isFunction(this.options.builder)) {
         contentElm = this.options.builder(item);
      } else {
         contentElm = this._builder(item);
      }
      rowElm.append(contentElm);
   },

   _builder: function(item) {
      var id = item.id ? item.id : '';
      var name = item.name ? item.name : 'No name available';
      var desc = item.desc ? item.desc : 'No description available';

      var linkElm = $('<a class="ui-list-item-link" href="#id=' + id + '"/>');
      $('<span class="ui-list-item-name">' + name + '</span>').appendTo(linkElm);
      $('<span class="ui-list-item-desc">' + desc + '</span>').appendTo(linkElm);
      return linkElm;
   }

});

}(jQuery));
