// Handles all the controller logic for the players page
$(function() {

var playersElm = $('.players-content');
var playersLst = $('.list-widget');

var playerElm = $('.player-content');
var enemiesElm = $('.enemies-content');
var enemiesTbl = $('.table-widget', enemiesElm);
var kitsElm = $('.kits-content');
var kitsTbl = $('.table-widget', kitsElm);
var mapsElm = $('.maps-content');
var mapsTbl = $('.table-widget', mapsElm);
var teamsElm = $('.teams-content');
var teamsTbl = $('.table-widget', teamsElm);
var vehiclesElm = $('.vehicles-content');
var vehiclesTbl = $('.table-widget', vehiclesElm);
var weaponsElm = $('.weapons-content');
var weaponsTbl = $('.table-widget', weaponsElm);

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the player identifier if available
      var id = e.getState('id');
      if (id) {

         // Hide the player index screen
         playersElm.hide();

         // Show the player statistics panel
         playerElm.show();
         $.mgr.requestPlayer(id);

         // Show the player enemies panel
         enemiesElm.show();
         $.mgr.requestEnemies(id);

         // Show the player kits panel
         kitsElm.show();
         $.mgr.requestKits(id);

         // Show the player maps panel
         mapsElm.show();
         $.mgr.requestMaps(id);

         // Show the player teams panel
         teamsElm.show();
         $.mgr.requestTeams(id);

         // Show the player vehicles panel
         vehiclesElm.show();
         $.mgr.requestVehicles(id);

         // Show the player weapons panel
         weaponsElm.show();
         $.mgr.requestWeapons(id);
      } else {

         // Hide the individual player panels
         playerElm.hide();
         enemiesElm.hide();
         kitsElm.hide();
         mapsElm.hide();
         teamsElm.hide();
         vehiclesElm.hide();
         weaponsElm.hide();

         // Show the players list screen
         playersElm.show();
         $.mgr.requestPlayers();
      }
   },

   requestPlayers: function() {

      // Display the loading indicator
      playersLst.list();
      playersLst.list('loading');

      // Configure the request options
      var options = {
         url: 'services/players',
         dataType: 'json',
         success: $.proxy($.mgr.onPlayers, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the index of all players
      $.ajax(options);
   },

   requestPlayer: function(id) {

      // Display the loading indicator
      weaponsTbl.table();
      weaponsTbl.table('loading');
      mapsTbl.table();
      mapsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/statistics',
         dataType: 'json',
         success: $.proxy($.mgr.onPlayer, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   requestEnemies: function(id) {
      enemiesTbl.table();
      enemiesTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/enemies',
         dataType: 'json',
         success: $.proxy($.mgr.onEnemies, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   requestKits: function(id) {
      kitsTbl.table();
      kitsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/kits',
         dataType: 'json',
         success: $.proxy($.mgr.onKits, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   requestMaps: function(id) {
      mapsTbl.table();
      mapsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/maps',
         dataType: 'json',
         success: $.proxy($.mgr.onMaps, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   requestTeams: function(id) {
      teamsTbl.table();
      teamsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/teams',
         dataType: 'json',
         success: $.proxy($.mgr.onTeams, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   requestVehicles: function(id) {
      vehiclesTbl.table();
      vehiclesTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/vehicles',
         dataType: 'json',
         success: $.proxy($.mgr.onVehicles, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },


   requestWeapons: function(id) {
      weaponsTbl.table();
      weaponsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id + '/weapons',
         dataType: 'json',
         success: $.proxy($.mgr.onWeapons, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected player
      $.ajax(options);
   },

   onPlayers: function(data) {

      // Update the header
      var headerElm = $('.common-header', playersElm);
      headerElm.text('Players (' + data.length + ')');

      // Populate the list with players
      playersLst.list('setRows', data);
   },

   onPlayer: function(data) {

      // Update the header
      var headerElm = $('.common-header', playerElm);
      headerElm.text(data.aliases[data.aliases.length - 1]);

      $('.player-photo', playerElm).attr('src',
            'images/players/' + data.id + '-large.jpg');

      var statsElm = $('.player-stats', playerElm);
      statsElm.empty();
      for (var key in data) {
         $('<li>' + key + ' ' + data[key] + '</li>').appendTo(statsElm);
      }
   },

   onEnemies: function(data) {

      // Populate the table with enemy results
      enemiesTbl.table('setColumns', data.columns);
      enemiesTbl.table('setRows', data.rows);
   },

   onKits: function(data) {

      // Populate the table with kit results
      kitsTbl.table('setColumns', data.columns);
      kitsTbl.table('setRows', data.rows);
   },

   onMaps: function(data) {

      // Populate the table with map results
      mapsTbl.table('setColumns', data.columns);
      mapsTbl.table('setRows', data.rows);
   },

   onTeams: function(data) {

      // Populate the table with team results
      teamsTbl.table('setColumns', data.columns);
      teamsTbl.table('setRows', data.rows);
   },

   onVehicles: function(data) {

      // Populate the table with vehicle results
      vehiclesTbl.table('setColumns', data.columns);
      vehiclesTbl.table('setRows', data.rows);
   },

   onWeapons: function(data) {

      // Populate the table with weapon results
      weaponsTbl.table('setColumns', data.columns);
      weaponsTbl.table('setRows', data.rows);
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
