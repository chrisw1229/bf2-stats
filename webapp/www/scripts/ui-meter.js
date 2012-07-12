(function($, undefined) {

$.widget('ui.meter', {

   // Configure the default widget options
   options: {
      max: 100,
      milestones: [],
      value: 0
   },

   _create: function() {
      var self = this;

      // Initialize the component attributes
      this.value = this.options.value;
      this.max = this.options.max;

      // Build the document model
      this.barElm = $('.ui-meter-bar', this.element);
      this.valueElm = $('.ui-meter-value', this.barElm);
      this.markerElm = $('.ui-meter-marker', this.element);
      this.milestoneElms = $('.ui-meter-milestone', this.barElm);

      // Bind the event handlers
      $(window).on('resize.meter', $.proxy(this._update, this));

      // Add any default milestones
      this.addMilestones(this.options.milestones);
   },

   destroy: function() {

      // Clear the event handlers
      $(window).off('resize.meter');

      // Destroy the document model
      this.milestoneElms.remove();
      this.milestoneElms = undefined;

      $.Widget.prototype.destroy.call(this);
   },

   addEvent: function(event) {
      this.value = event.time;
      if (event.team) {
         this.addMilestones(event);
      } else {
         this._update();
      }
   },

   addMilestones: function(milestones) {
      milestones = ($.isArray(milestones) ? milestones : [milestones]);

      for (var i = 0; i < milestones.length; i++) {
         this._createMilestoneElm(milestones[i]);
      }
      this.milestoneElms = $('.ui-meter-milestone', this.barElm);
      this._update();
   },

   reset: function(max) {
      this.value = 0;
      this.max = (max != undefined ? max : this.max);

      this.milestoneElms.remove();
      this._update();
   },

   _update: function() {

      // Adjust the position of the progress bar value and marker
      var maxW = this.element.width();
      var markerW = this.markerElm.width();
      var barW = (this.element.width() - markerW);
      var markerL = barW * (this.value / this.max);
      this.valueElm.css('width', markerL);
      this.markerElm.css({ left: markerL, visibility: 'visible' });

      // Display any milestones that have occurred
      this.milestoneElms.each(function(index, item) {
         var itemElm = $(item);
         var model = itemElm.data('model');
         if (this.value >= model.time) {
            var pos = barW * (model.time / this.max) - (itemElm.width() / 2);
            itemElm.css('left', pos);
            itemElm.show();
         } else {
            itemElm.hide();
         }
      });

      // Update the time remaining tool tip
      var remaining = this.max - this.value;
      var mins = remaining >= 60 ? Math.round(remaining / 60) : 0;
      var secs = Math.round(remaining % 60);
      var time = mins + ':' + (secs < 10 ? '0' : '') + secs;
      this.barElm.attr('title', 'Time Remaining: ' + time);
   },

   _createMilestoneElm: function(model) {
      var milestoneElm = $('<div class="ui-meter-milestone icon-team icon-team-'
            + model.team + '"/>').appendTo(this.barElm);
      milestoneElm.data('model', model);
      milestoneElm.attr('title', model.desc);
      milestoneElm.hide();
      return milestoneElm;
   }

});

}(jQuery));
