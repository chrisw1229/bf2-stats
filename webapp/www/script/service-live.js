// Provides dynamic network communication with the server
(function($) {

// Register the communication object as a jQuery extension
$.extend({ service: {

   baseUrl: 'live', // The address of the communication service
   params: {}, // Optional set of parameters to add to the request
   threshold: 0, // Stores the last update threshold from the server
   errors: 0, // The number of consecutive communication errors
   producer: undefined, // An optional function that produces synthetic packets

   // Makes an update request to the server to get new data
   refresh: function(type, all) {

      // Build a list of request parameters
      var params = { threshold: (all ? 0 : this.threshold) };
      if (type) {
         params.packet_type = type;
      }
      $.extend(params, this.params);

      // Configure the request options
      var options = {
         url: this.baseUrl,
         data: params,
         dataType: 'json',
         cache: false,
         success: $.proxy(this._onSuccess, this),
         error: $.proxy(this._onError, this),
         complete: $.proxy(this._onComplete, this)
      };

      // Check whether a synthetic packet producer is registered
      if (this.producer) {

         // Get the next packet from a local function
         this._onSuccess(this.producer(options));
         this._onComplete();
      } else {

         // Send the request to the server
         $.ajax(options);
      }
   },

   // Handles updated data responses from the server
   _onSuccess: function(data, status) {

      // Clear any previous errors
      this.errors = 0;

      // Process all the packets received from the server
      for (var i = 0; i < data.length; i++) {
         var packet = data[i];

         // Check if this is a threshold packet
         if (packet.type == 'threshold') {
            this.threshold = packet.values;
         } else {

            // Pass the packet to all registered listeners
            try {
               $($.service).trigger(packet);
            } catch(err) {
               $.log.error('Error processing service packet: ' + packet.type, err);
            }
         }
      }
   },

   // Handles error responses from the server
   _onError: function(request, status, error) {
      this.errors++;
      $.log.error('Error connecting to server', error);
   },

   // Handles cleanup after an update completes
   _onComplete: function(request, status) {

      // Calculate the delay until the next update
      // Retry quickly for initial errors then slow down for repeated errors
      var delay = (1 + (this.errors < 3 ? this.errors : 59)) * 1000;

      // Request the next set of updates from the server
      setTimeout($.proxy(function() { this.refresh(); }, this), delay);
   }

}});

})(jQuery);
