(function($, undefined) {

$.widget('ui.message', {

   // Configure the default widget options
   options: {
      maxMessages: 5
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

   clearMessages: function() {
      for (var i = 0; i < this.itemElms.length; i++) {
         this._unloadItem(this.itemElms.eq(i));
      }
      this.messages = [];
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
      var weapon = attacker ? attacker.weapon : undefined;

      var attackerElm = $('.ui-message-attacker', itemElm);
      var weaponElm = $('.ui-message-weapon', itemElm);
      var victimElm = $('.ui-message-victim', itemElm);

      if (attacker) {
         itemElm.attr('class', 'ui-message-item'
               + ' ui-message-team-' + attacker.team_id);

         attackerElm.text(attacker.name);
         attackerElm.show();

         weaponElm.text('[' + (weapon ? weapon : '?') + ']');
         weaponElm.show();

         victimElm.text(victim.name);
      } else {
         itemElm.attr('class', 'ui-message-item'
               + ' ui-message-team-'
               + (victim.team_id ? victim.team_id : 'none'));

         attackerElm.text('');
         attackerElm.hide();
         weaponElm.text('');
         weaponElm.hide();

         var victimMsg;
         if (victim.suicide) {
            victimMsg = ' suicided.';
         } else if (victim.type) {
            victimMsg = ' was destroyed.';
         } else {
            victimMsg = ' is no more.';
         }
         victimElm.text(victim.name + victimMsg);
      }
      itemElm.show();
   },

   _unloadItem: function(itemElm) {
      $('.ui-message-attacker', itemElm).text('');
      $('.ui-message-weapon', itemElm).text('');
      $('.ui-message-victim', itemElm).text('');
      itemElm.hide();
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
