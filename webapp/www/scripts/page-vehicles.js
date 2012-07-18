// Handles all the controller logic for the vehicles page
$(function() {

var vehiclesElm = $('.vehicles-content');
var listElm = $('.list-widget');

var vehicleElm = $('.vehicle-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the vehicle identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual vehicle screen
         vehiclesElm.hide();
         vehicleElm.show();
         $.mgr.requestVehicle(id);
      } else {

         // Show the vehicles list screen
         vehicleElm.hide();
         vehiclesElm.show();
         $.mgr.requestVehicles();
      }
   },

   requestVehicles: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/vehicles',
         dataType: 'json',
         success: $.proxy($.mgr.onVehicles, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected vehicle
      $.ajax(options);
   },

   requestVehicle: function(id) {

      // Display the loading indicator
      tableElm.table();
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/vehicles/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onVehicle, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected vehicle
      $.ajax(options);
   },

   onVehicles: function(data) {

      // Update the header
      var headerElm = $('.common-header', vehiclesElm);
      headerElm.text('Vehicles (' + data.length + ')');

      // Populate the list with vehicles
      listElm.list('setRows', data);
   },

   onVehicle: function(data) {

      // Update the header
      var headerElm = $('.common-header', vehicleElm);
      headerElm.text('Vehicle - ' + data.name);

      // Populate the table with vehicle results
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
