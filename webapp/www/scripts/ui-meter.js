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
      this.controlPointsElm = $('.ui-meter-control-points', this.element);

      // Bind the event handlers
      $(window).on('resize.meter', $.proxy(this._onResize, this));
   },

   destroy: function() {

      // Clear the event handlers
      $(window).off('resize.meter');

      // Destroy the document model
      this.controlPointsElm.empty();

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

   addControlPoint: function(model) {

      // Only add markers when a team fully controls a point
      if (model.state != 'top' || model.team.length == 0) {
         return;
      }

      this._createControlPointElm(model);
      this._update();
   },

   addPackets: function(packets) {
      if (packets == undefined) {
         return;
      }
      packets = $.isArray(packets) ? packets : [packets];

      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.type == 'CP') {
            this.addControlPoint(packet.control_point);
         }
      }
   },

   clearMarkers: function() {
      this.controlPointsElm.empty();
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

      // Display any control points that have occurred
      var value = this.options.value;
      var max = this.options.max;
      $('.ui-meter-control-point', this.controlPointsElm).each(function(index, item) {
         var itemElm = $(item);
         var model = itemElm.data('model');
         if (value >= model.time) {
            var pos = Math.round(barW * (model.time / max) - (itemElm.width() / 2));
            itemElm.css('left', pos);
            itemElm.show();
         } else {
            itemElm.hide();
         }
      });

      // Update the time remaining tool tip
      var remaining = this.options.max - this.options.value;
      var mins = remaining >= 60 ? Math.floor(remaining / 60) : 0;
      var secs = Math.round(remaining % 60);
      var time = mins + ':' + (secs < 10 ? '0' : '') + secs;
      this.markerElm.attr('title', 'Time Remaining: ' + time);
   },

   _createControlPointElm: function(model) {
      var controlPointElm = $('<div class="ui-meter-control-point icon-team icon-team-'
            + model.team + '"/>').appendTo(this.controlPointsElm);
      controlPointElm.data('model', model);
      controlPointElm.hide();
      return controlPointElm;
   },

   _onResize: function(e) {
      this._update();
   }

});

}(jQuery));
