// Handles all the controller logic for the awards page
$(function() {

var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   requestResults: function(id) {

      // Display the loading indicator
      tableElm.table({ showAll: true });
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/leaderboard',
         dataType: 'json',
         success: $.proxy($.mgr.onResults, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the leaderboard
      $.ajax(options);
   },

   onResults: function(data) {

      // Populate the table with award results
      tableElm.table('setColumns', data.columns);
      tableElm.table('setRows', data.rows);
   },

   onError: function(request, status, error) {
   
   }

}});

// Load the custom jQuery user interface components
$('.common-nav').nav();

// Request the initial results
$.mgr.requestResults();

});
