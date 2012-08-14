(function($, undefined) {

$.widget('ui.message', {

   // Configure the default widget options
   options: {
      maxMessages: 4
   },

   _create: function() {
      this.messages = [];

      this.element.addClass('ui-message');

      // Build the list items to hold the messages
      this.listElm = $('.ui-message-list', this.element);
      this.prototypeElm = $('.ui-message-item', this.listElm).remove();
      for (var i = 0; i < this.options.maxMessages; i++) {
         this.prototypeElm.clone().appendTo(this.listElm);
      }
      this.itemElms = this.listElm.children();

      // Start a timer to clean up old items
      this._cleanItems();
   },

   destroy: function() {

      // Stop the clean up timer
      clearTimeout(this.running);
      this.running = undefined;

      // Destroy the document model
      this.element.removeClass('ui-message');
      this.itemElms.remove();
      this.prototypeElm.appendTo(this.listElm);
      this.prototypeElm = undefined;

      $.Widget.prototype.destroy.call(this);
   },

   addPackets: function(packets) {
      packets = ($.isArray(packets) ? packets : [packets]);

      // Update the displayed messages
      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.type == 'KL') {
            this.addMessage(packet.attacker, packet.victim);
         }
      }
   },

   addMessage: function(attacker, victim) {

      // Create a model to store the message info
      var message = {
         attacker: attacker,
         victim: victim,
         timestamp: new Date().getTime()
      }

      // Cache the message for display
      this.messages.push(message);

      // Remove the oldest message when the max is exceeded
      if (this.messages.length > this.options.maxMessages) {
         this.messages.splice(0, 1);
      }

      // Update the displayed messages
      this._refresh();
   },

   _refresh: function() {

      // Update the displayed messages
      for (var i = 0; i < this.messages.length; i++) {
         var message = this.messages[i];
         var itemElm = this.itemElms.eq(i);
         this._loadItem(itemElm, message.attacker, message.victim);
      }

      // Clear out extra items that are not currently needed
      for (var i = this.messages.length; i < this.itemElms.length; i++) {
         this._unloadItem(this.itemElms.eq(i));
      }
   },

   _loadItem: function(itemElm, attacker, victim) {

      // Update the attacker elements
      var attackerElm = $('.ui-message-attacker', itemElm);
      attackerElm.text(attacker ? attacker.name : '');
      attackerElm.attr('class', 'ui-message-name ui-message-attacker'
            + ' ui-message-team-' + (attacker ? attacker.team_id : ''));

      // Update the kill type symbol
      var symbolElm = $('.ui-message-symbol', itemElm);
      symbolElm.html('&#9658;');
      symbolElm.attr('class', 'ui-message-symbol'
            + ' ui-message-team-' + (attacker ? attacker.team_id : victim.team_id));

      // Update the victim elements
      var victimElm = $('.ui-message-victim', itemElm);
      victimElm.text(victim.name);
      victimElm.attr('class', 'ui-message-name ui-message-victim'
            + ' ui-message-team-' + victim.team_id);
   },

   _unloadItem: function(itemElm) {
      $('.ui-message-name', itemElm).text('');
      $('.ui-message-symbol', itemElm).text('');
   },

   _cleanItems: function() {

      // Get the current time stamp
      var now = new Date().getTime();

      // Check for any expired messages
      for (var i = this.messages.length - 1; i >= 0; i--) {

         // Remove messages older than 5 seconds
         if (now - this.messages[i].timestamp >= 5000) {
            this.messages.splice(i, 1);
         }
      }
      this._refresh();

      // Schedule the clean operation in 5 seconds
      this.running = setTimeout($.proxy(this._cleanItems, this), 5000);
   }

});

}(jQuery));
