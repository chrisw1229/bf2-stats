(function($) {

$.widget('ui.logger', {

   // Configure the default widget options
	options: {
	},

	_create: function() {

      // Build the document model
      this.element.addClass('ui-logger');
      this.bodyDiv = $('<div class="ui-widget-content ui-corner-all ui-logger-body"/>').appendTo(this.element);
      this.iconDiv = $('<div class="ui-icon ui-logger-icon"/>').appendTo(this.bodyDiv);
      this.msgDiv = $('<div class="ui-logger-message"/>').appendTo(this.bodyDiv);

      // Bind the event handlers
      $($.log).on('log', $.proxy(this._onLog, this));
   },

   destroy: function() {

      // Clear the event handlers
      $($.log).off('log');

      // Destroy the document model
      this.element.removeClass('ui-logger');
      this.bodyDiv.remove();

      $.widget.prototype.destroy.apply(this, arguments);
   },

   _onLog: function(event) {

      // Construct the log statement
      var text = event.msg + (event.exc ? '\n' + event.exc : '');

      // Display debug statements as alerts
      if (event.type == 'debug') {
         alert('DEBUG: ' + text);
         return;
      }

      if (event.type == 'error') {
         this.bodyDiv.removeClass('ui-state-highlight').addClass('ui-state-error');
         this.iconDiv.removeClass('ui-icon-info').addClass('ui-icon-alert');
      } else {
         this.bodyDiv.removeClass('ui-state-error').addClass('ui-state-highlight');
         this.iconDiv.removeClass('ui-icon-alert').addClass('ui-icon-info');
      }

      // Set the log message text
      this.msgDiv.text(text);

      // Display the log
      this.element.css({ left: ($(window).width() - this.element.width()) - 5,
            top: ($(window).height() - this.element.height()) - 5 });
      this.element.show('slide', { direction: 'down' }, 'slow' );

      // Hide the log after a delay unless a new log comes in
      var self = this;
      var logId = setTimeout(function() {
         if (self.logId == logId) {
            self.element.hide('slide', { direction: 'down' }, 'slow');
         }
      }, 5000);
      this.logId = logId;
   }

});


})(jQuery);

