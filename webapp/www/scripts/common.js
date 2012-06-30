// Extends the jQuery object with additional utility functions
(function($) {

// Register the log object as a jQuery extension
$.extend({ log: {

   enabled: true,

   info: function(msg, exc) {
      if (this.enabled) {
         $(this).trigger({ type: 'log', category: 'info', msg: msg, exc: exc });
      }
   },

   error: function(msg, exc) {
      if (this.enabled) {
         $(this).trigger({ type: 'log', category: 'error', msg: msg, exc: exc });
      }
   },

   debug: function(message, exc) {
      if (this.enabled) {
         $(this).trigger({ type: 'log', category: 'debug', msg: msg, exc: exc });
      }
   }

}});

$.extend({

   // This function gets parameter value from a URL
   getUrlParam: function(url, key) {
      var pos = url.indexOf('?');
      if (pos < 0) {
         return null;
      }

      var query = url.substring(pos + 1);
      var params = query.split('&');
      for (var i = 0; i < params.length; i++) {
         var param = params[i].split('=');
         if (param[0] == key) {
            return (param.length == 1 ? true : param[1]);
         }
      }
      return null;
  }

});

})(jQuery);
