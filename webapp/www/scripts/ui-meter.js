(function($, undefined) {

$.widget('ui.meter', {

   // Configure the default widget options
   options: {
      max: 100,
      value: 0
   },

   _create: function() {

      // Build the document model
      this.barElm = $('.ui-meter-bar', this.element);
      this.valueElm = $('.ui-meter-value', this.barElm);
      this.markerElm = $('.ui-meter-marker', this.element);
      this.flagActionsElm = $('.ui-meter-flag-actions', this.element);

      // Bind the event handlers
      $(window).on('resize.meter', $.proxy(this._onResize, this));
   },

   destroy: function() {

      // Clear the event handlers
      $(window).off('resize.meter');

      // Destroy the document model
      this.flagActionsElm.empty();

      $.Widget.prototype.destroy.call(this);
   },

   _setOption: function(key, value) {
      $.Widget.prototype._setOption.apply(this, arguments);

      // Check whether the value changed
      if (key === 'value') {

         // Make sure the value stays in range
         if (this.options.value > this.options.max) {
            this.options.value = this.options.max;
         }

         // Refresh the display
         this._update();
      }
   },

   addFlagAction: function(model) {
      console.log(model.time + " " + model.action_type);
      if (model.action_type != 'capture' && model.action_type != 'neutralize') {
         return;
      }

      this._createFlagActionElm(model);
      this._update();
   },

   addPackets: function(packets) {
      if (packets == undefined) {
         return;
      }
      packets = $.isArray(packets) ? packets : [packets];

      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.type == 'FA') {
            this.addFlagAction(packet);
         }
      }
   },

   clearMarkers: function() {
      this.flagActionsElm.empty();
      this._update();
   },

   _update: function() {

      // Adjust the position of the progress bar value and marker
      var maxW = this.element.width();
      var markerW = this.markerElm.width();
      var barW = (this.element.width() - markerW);
      var markerL = Math.round(barW * (this.options.value / this.options.max));
      this.valueElm.css('width', markerL);
      this.markerElm.css({ left: markerL, visibility: 'visible' });

      // Display any flag actions that have occurred
      var value = this.options.value;
      var max = this.options.max;
      var self = this;
      $('.ui-meter-flag-action', this.flagActionsElm).each(function(index, item) {
         var itemElm = $(item);
         var model = itemElm.data('model');
         if (value >= model.time) {
            var pos = Math.round(barW * (model.time / max) - (itemElm.width() / 2));
            itemElm.css('left', pos);
            itemElm.attr('title', model.player.name
                  + ' [' + model.action_type + ']'
                  + ' @ ' + self._formatTime(model.time));
            itemElm.show();
         } else {
            itemElm.hide();
         }
      });

      // Update the time remaining tool tip
      var remaining = this.options.max - this.options.value;
      var time = this._formatTime(remaining);
      this.markerElm.attr('title', 'Time Remaining: ' + time);
   },

   _createFlagActionElm: function(model) {
      var team_id;
      if (model.action_type == 'capture') {
         team_id = model.player.team_id
      } else {
         team_id = 'none';
      }
      var flagActionElm = $('<div class="ui-meter-flag-action ui-meter-team-'
            + team_id + '"/>').appendTo(this.flagActionsElm);
      flagActionElm.data('model', model);
      flagActionElm.hide();
      return flagActionElm;
   },

   _formatTime: function(time) {
      var mins = time >= 60 ? Math.floor(time / 60) : 0;
      var secs = Math.round(time % 60);
      return mins + ':' + (secs < 10 ? '0' : '') + secs;
   },

   _onResize: function(e) {
      this._update();
   }

});

}(jQuery));
