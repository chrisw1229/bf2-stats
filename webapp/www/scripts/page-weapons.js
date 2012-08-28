// Handles all the controller logic for the weapons page
$(function() {

var weaponsElm = $('.weapons-content');
var listElm = $('.list-widget');

var weaponElm = $('.weapon-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the weapon identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual weapon screen
         weaponsElm.hide();
         weaponElm.show();
         $.mgr.requestWeapon(id);
      } else {

         // Show the weapons list screen
         weaponElm.hide();
         weaponsElm.show();
         $.mgr.requestWeapons();
      }
   },

   requestWeapons: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/weapons',
         dataType: 'json',
         success: $.proxy($.mgr.onWeapons, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected weapon
      $.ajax(options);
   },

   requestWeapon: function(id) {

      // Display the loading indicator
      tableElm.table({ showAll: true });
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/weapons/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onWeapon, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected weapon
      $.ajax(options);
   },

   onWeapons: function(data) {

      // Update the header
      var headerElm = $('.common-header', weaponsElm);
      headerElm.text('Weapons (' + data.length + ')');

      // Populate the list with weapons
      listElm.list('setRows', data);
   },

   onWeapon: function(data) {

      // Update the header
      var headerElm = $('.common-header-title', weaponElm);
      headerElm.text(data.name);

      // Populate the table with weapon results
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
