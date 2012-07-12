// Handles all the controller logic for the kits page
$(function() {

var kitsElm = $('.kits-content');
var listElm = $('.list-widget');

var kitElm = $('.kit-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the kit identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual kit screen
         kitsElm.hide();
         kitElm.show();
         $.mgr.requestKit(id);
      } else {

         // Show the kits list screen
         kitElm.hide();
         kitsElm.show();
         $.mgr.requestKits();
      }
   },

   requestKits: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/kits',
         dataType: 'json',
         success: $.proxy($.mgr.onKits, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected kit
      $.ajax(options);
   },

   requestKit: function(id) {

      // Display the loading indicator
      tableElm.table();
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/kits/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onKit, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected kit
      $.ajax(options);
   },

   onKits: function(data) {

      // Update the header
      var headerElm = $('.common-header', kitsElm);
      headerElm.text('Kits (' + data.length + ')');

      // Populate the list with kits
      listElm.list('setRows', data);
   },

   onKit: function(data) {

      // Update the header
      var headerElm = $('.common-header', kitElm);
      headerElm.text('Kit - ' + data.name);

      // Populate the table with kit results
      tableElm.table('setColumns', data.columns);
      tableElm.table('setRows', data.rows);
   },

   onError: function(request, status, error) {
   
   }

}});

// Callback when the URL fragment changes
$(window).on('hashchange', $.mgr.onHistory);

// Load the custom jQuery user interface components
$('.common-nav').nav();

// Trigger the history event on initial page load
$(window).trigger('hashchange');

});
