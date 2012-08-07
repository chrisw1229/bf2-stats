(function($, undefined) {

$.widget('ui.ticker', {

   // Configure the default widget options
   options: {
   },

   _create: function() {
      this.models = {};
      this.sorted = [];
      this.loadIndex = 0;

      // Build the document model
      this.element.addClass('ui-widget-content ui-ticker');
      this.itemsElm = $('.ui-ticker-items', this.element);
      this.nextElm = $('.ui-ticker-nav', this.element);

      // Bind the event handlers
      this.nextElm.on('click', $.proxy(this._onNextClick, this));
      this.itemsElm.on('mouseover', $.proxy(this._onItemMouseOver, this));
      this.itemsElm.on('mouseout', $.proxy(this._onItemMouseOut, this));
      $(window).on('resize.ticker', $.proxy(this._onResize, this));

      this._reset();
   },

   destroy: function() {

      // Clear the event handlers
      this.nextElm.off('click mouseover mouseout');
      this.itemsElm.off('mouseover mouseout');
      $(window).off('resize.ticker');

      // Destroy the document model
      this.element.removeClass('ui-ticker');

      $.Widget.prototype.destroy.call(this);
   },

   clear: function() {

      // Check if there is any data to clear
      if (this.sorted.length == 0) {
         return;
      }

      // Reset all the model variables
      this.models = {};
      this.sorted = [];
      this.loadIndex = 0;

      // Reset the ticker elements
      this.maxW = 0;
      this._reset();
   },

   next: function() {

      // Make sure there are items loaded
      if (this.sorted.length >= 0) {

         // Move the ticker by one item immediately
         this.stop();
         this.navigating = true;
         this.start();
         this.navigating = undefined;
      }
   },

   start: function() {
      if (!this.running) {

         // Schedule the ticker animation sometime in the future
         var self = this;
         this.running = setTimeout(function() { 

            // Move the ticker at the configured frame rate
            self.sliding = setInterval(function() { self._animate(); },
                  self.anim.rate);
         },

         // Animate immediately if navigating otherwise use the configured time
         (this.navigating ? 0 : this.anim.pause));
      }
   },

   stop: function() {

      // Check whether the animation is active
      if (this.running) {

         // Cleanup the animation timers
         clearTimeout(this.running);
         this.running = undefined;
         clearInterval(this.sliding);
         this.sliding = undefined;
      }
   },

   update: function(models) {
      models = ($.isArray(models) ? models : [models]);

      // Apply the updates to the model cache
      for (var i = 0; i < models.length; i++) {
         var newModel = models[i];

         // Check if the new model is already stored
         if (this.models[newModel.id]) {

            // Check if the new model is being removed
            if (newModel.team == "") {

               // Remove the existing model
               this._removeModel(newModel);
            } else {

               // Update the existing model
               this._updateModel(newModel);
            }
         } else {

            // Add a completely new model
            this._addModel(newModel);
         }
      }
   },

   _addModel: function(model) {

      // Store the model for future lookup
      this.models[model.id] = model;

      // Insert the model at its sorted position
      var index = this.sorted.length;
      for (var i = 0; i < this.sorted.length; i++) {
         if (model.name < this.sorted[i].name) {
            index = i;
            break;
         }
      }
      this.sorted.splice(index, 0, model);

      // Adjust the load index if the model was inserted before it
      if (index < this.loadIndex) {
         this.loadIndex = (this.loadIndex < this.sorted.length - 1 ? this.loadIndex + 1 : 0);
      }

      // Load the model into the displayed group if it has room
      if (this.group && this.anim && this.sorted.length - 1 < this.anim.count) {
         this.loadIndex = 0;
         this._loadGroup(this.group);
      }
   },

   _animate: function() {
      if (!this.running) {
         return;
      }

      // Move the group 1 until it surpasses the left screen bounds
      if (this.anim.x1 > this.anim.outPos) {
         this.anim.x1 -= this.anim.speed;
         this.group1.css("left", this.anim.x1);
         this.group = this.group1;
      }

      // Reset group 2 once group 1 reaches the left screen bounds
      if (this.anim.state != 1) {
         if (this.anim.x1 + this.anim.groupW <= this.anim.maxW) {
         this.anim.x2 = this.anim.x1 + this.anim.groupW + this.anim.speed;
         this._loadGroup(this.group2);
         this.group2.show();
         this.anim.state = 1;
         }
      }

      // Move group 2 until it surpasses the left screen bounds
      if (this.anim.state != 0) { 
         if (this.anim.x2 > this.anim.outPos) {
         this.anim.x2 -= this.anim.speed;
         this.group2.css("left", this.anim.x2);
         this.group = this.group2;
         }
      }

      // Reset group 1 once group 2 reaches the left screen bounds
      if (this.anim.state != 2
            && this.anim.x2 + this.anim.groupW <= this.anim.maxW) {
         this.anim.x1 = this.anim.x2 + this.anim.groupW;
         this._loadGroup(this.group1);
         this.anim.state = 2;
      }

      // Pause for a few seconds after sliding one full item
      this.anim.moved += this.anim.speed;
      if (this.anim.moved >= this.anim.itemW) {
         this.anim.moved = 0;
         this.stop();
         this.start();
      }
   },

   _loadGroup: function(group) {

      // Load all the ticker model data for the given group
      var self = this;
      var count = 0;
      $('.ui-ticker-item', group).each(function() {
         var itemElm = $(this);

         // Check if there is enough data to display the item
         if (count < self.sorted.length) {

            // Make sure the element is fully visible
            itemElm.show();
            itemElm.fadeTo(0, 1.0);

            // Make sure the load index stays within range
            if (self.loadIndex < 0 || self.loadIndex >= self.sorted.length) {
               self.loadIndex = 0;
            }

            // Load the model into the element
            var model = self.sorted[self.loadIndex++];
            self._loadModel(this, model);
            count++;
         } else {

            // Hide the element since it will be empty
            itemElm.hide();
         }
      });
   },

   _loadModel: function(itemElm, model) {

      // Load all the basic values for the given model
      $('.ui-ticker-item-name', itemElm).text(model.name);
      $('.ui-ticker-item-photo', itemElm).css('background-image',
            'url(' + model.photo + ')');

      // Check whether the current model is a spectator
      var team = (model.team && model.team.length > 0 ? model.team.charAt(0) : '').toLowerCase();
      if (team != 's') {

         // Load the player game place
         $('.ui-ticker-place-value', itemElm).text(model.place);

         // Load the player military rank
         var rankTip = 'Rank: ';
         if (model.rank >= 0 && model.rank < this.ranks.length) {
            rankTip += this.ranks[model.rank];
         } else {
            rankTip += 'Unknown';
         }
         $('.icon-rank', itemElm).attr('class', 'icon-rank icon-rank-'
               + model.rank + ' ui-ticker-rank').attr('title', rankTip);

         // Load the player team
         var teamTip = 'Team: ';
         if (model.team && this.teams[model.team]) {
            teamTip += this.teams[model.team];
         } else {
            teamTip += 'Unknown';
         }
         $('.icon-team', itemElm).attr('class', 'icon-team icon-team-'
               + model.team + ' ui-ticker-team').attr('title', teamTip);

         // Show all the icon content
         $('.ui-ticker-item-icons', itemElm).show();

         // Load the trend content
         var trendState, trendIcon, trendTip = 'Trend: ';
         if (model.trend == '+') {
            trendState = 'highlight';
            trendIcon = 'arrow-n';
            trendTip += 'Improving'
         } else if (model.trend == '-') {
            trendState = 'error';
            trendIcon = 'arrow-s';
            trendTip += 'Declining'
         } else if (model.trend == '') {
            trendState = '';
            trendIcon = 'minus';
            trendTip += 'Unchanged';
         } else {
            trendTip += 'Unknown';
         }
         $('.ui-ticker-trend', itemElm).attr('class', 'ui-state-' + trendState
               + ' ui-ticker-trend');
         $('.ui-ticker-trend-icon', itemElm).attr('class',
               'ui-icon ui-icon-circle-' + trendIcon + ' ui-ticker-trend-icon')
               .attr('title', trendTip);
         $('.ui-ticker-trend', itemElm).show();

         // Load all the numeric content
         $('.ui-ticker-kills .ui-ticker-stat-value', itemElm).text(model.kills);
         $('.ui-ticker-deaths .ui-ticker-stat-value', itemElm).text(model.deaths);
         $('.ui-ticker-inflicted .ui-ticker-stat-value', itemElm).text(model.inflicted);
         $('.ui-ticker-received .ui-ticker-stat-value', itemElm).text(model.received);
         $('.ui-ticker-stats', itemElm).show();
         $('.ui-ticker-spec', itemElm).hide();
      } else {

         // Just show the spectator label
         $('.ui-ticker-item-icons', itemElm).hide();
         $('.ui-ticker-trend', itemElm).hide();
         $('.ui-ticker-stats', itemElm).hide();
         $('.ui-ticker-spec', itemElm).show();
      }

      // Update the mapping between element and model
      $(itemElm).data('model', model);
   },

   _onResize: function(e) {
      this._reset();
   },

   _onItemMouseOver: function(e) {
   
   },

   _onItemMouseOut: function(e) {
   
   },

   _onNextClick: function(e) {
      this.next();
   },

   _refreshModel: function(model) {

      // Reload the model attributes if it is currently being displayed
      var self = this;
      $('.ui-ticker-item', this.itemsElm).each(function() {
         var itemModel = $(this).data('model');
         if (itemModel && itemModel.id == model.id) {
            self._loadModel(this, model);
         }
      });
   },

   _removeModel: function(model) {

      // Remove the model from the local cache
      delete this.models[model.id];

      // Remove the model from its sorted position
      var index = 0;
      for (var i = 0; i < this.sorted.length; i++) {
         if (item.id == this.sorted[i].id) {
            index = i;
            break;
         }
      }
      this.sorted.splice(index, 1);

      // Adjust the load index if the model was removed before it
      if (index < this.loadIndex) {
         this.loadIndex = (this.loadIndex > 0 ? this.loadIndex - 1 : 0);
      } else if (this.loadIndex >= this.sorted.length) {
         this.loadIndex = 0;
      }

      // Unload the model if it is currently being displayed
      this._unloadModel(model);
   },

   _reset: function() {

      // Only recompute the ticker bounds if the width changed
      var maxW = this.element.width();
      if (this.maxW == maxW) {
         return;
      }
      this.maxW = maxW;

      // Stop the current ticker animation if applicable
      this.stop();

      // Grab and measure the ticker item prototype at startup
      if (!this.prototypeElm) {
         this.prototypeElm = $('.ui-ticker-item', this.itemsElm);
         var protoW = this.prototypeElm.outerWidth(true);
         this.prototypeElm.remove();
         this.prototypeElm.data('width', protoW);
      }

      // Calculate the number of ticker items that will fit on screen at once
      var itemW = this.prototypeElm.data('width');
      var count = Math.ceil(maxW / itemW);

      // Clear any previous ticker items
      this.itemsElm.empty();

      // Generate a group to hold a set of ticker items
      this.group1 = $('<div class="ui-ticker-slider"/>').appendTo(this.itemsElm);
      this.group1.css({ left: 0, width: (itemW * count) });

      // Generate the ticker items
      for (var i = 0; i < count; i++) {
         var itemElm = this.prototypeElm.clone().appendTo(this.group1);
         itemElm.css('left', i * itemW);
      }

      // Make a copy of the group to rotate through the ticker
      this.group2 = this.group1.clone().appendTo(this.itemsElm);
      this.group2.hide();
      this.group = this.group2;

      // Fill the first group with data
      this._loadGroup(this.group1);

      // Configure the ticker animation
      var groupW = this.group1.width();
      this.anim = {
         rate: 100, speed: 52, pause: 4000,
         maxW: maxW, groupW: groupW, itemW: itemW,
         inPos: (maxW - groupW), outPos: (-1 * groupW),
         x1: 0, x2: groupW, moved: 0, state: 0, count: count
      };

      // Start the ticker animation
      this.start();
   },

   _unloadModel: function(model) {

      // Fade out the model if it is currently being displayed
      $('.ui-ticker-item', this.itemsElm).each(function() {
         var itemElm = $(this);
         var itemModel = itemElm.data('model');
         if (itemModel && itemModel.id == model.id) {
            itemElm.fadeTo('slow', 0.3);
            itemElm.removeData('model');
         }
      });
   },

   _updateModel: function(model) {

      // Check whether the model name changed
      var oldModel = this.models[model.id];
      if (model.name && oldModel.name != model.name) {

         // Remove the model from its current sorted position
         var oldIndex = 0;
         for (var i = 0; i < this.sorted.length; i++) {
            if (model.id == this.sorted[i].id) {
               oldIndex = i;
               break;
            }
         }
         this.sorted.splice(oldIndex, 1);

         // Add the model to its new sorted position
         var newIndex = this.sorted.length;
         for (var i = 0; i < this.sorted.length; i++) {
            if (model.name < this.sorted[i].name) {
               newIndex = i;
               break;
            }
         }
         this.sorted.splice(newIndex, 0, oldModel);

         // Adjust the load index if the model moved across the load index
         if (oldIndex < this.loadIndex && newIndex >= this.loadIndex) {
            this.loadIndex = (this.loadIndex > 0 ? this.loadIndex - 1 : 0);
         } else if (newIndex < this.loadIndex && oldIndex >= this.loadIndex) {
            this.loadIndex = (this.loadIndex < this.sorted.length - 1 ? this.loadIndex + 1 : 0);
         }
      }

      // Merge the updated model into the cached model
      $.extend(oldModel, model);

      // Update the associated element if it is being displayed
      this._refreshModel(oldModel);
   }

});

}(jQuery));
