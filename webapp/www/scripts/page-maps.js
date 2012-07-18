// Handles all the controller logic for the maps page
$(function() {

var mapsElm = $('.maps-content');
var listElm = $('.list-widget');

var mapElm = $('.map-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the map identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual map screen
         mapsElm.hide();
         mapElm.show();
         $.mgr.requestMap(id);
      } else {

         // Show the maps list screen
         mapElm.hide();
         mapsElm.show();
         $.mgr.requestMaps();
      }
   },

   requestMaps: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/maps',
         dataType: 'json',
         success: $.proxy($.mgr.onMaps, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected map
      $.ajax(options);
   },

   requestMap: function(id) {

      // Display the loading indicator
      tableElm.table();
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/maps/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onMap, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected map
      $.ajax(options);
   },

   onMaps: function(data) {

      // Update the header
      var headerElm = $('.common-header', mapsElm);
      headerElm.text('Maps (' + data.length + ')');

      // Populate the list with maps
      listElm.list('setRows', data);
   },

   onMap: function(data) {

      // Update the header
      var headerElm = $('.common-header', mapElm);
      headerElm.text('Map - ' + data.name);

      // Populate the table with map results
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
