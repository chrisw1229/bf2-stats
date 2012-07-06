// Handles all the controller logic for the players page
$(function() {

var playersElm = $('.players-content');
var playersLst = $('.list-widget');

var playerElm = $('.player-content');
var weaponsElm = $('.weapons-content');
var weaponsTbl = $('.table-widget', weaponsElm);
var enemiesElm = $('.enemies-content');
var enemiesTbl = $('.table-widget', enemiesElm);
var mapsElm = $('.maps-content');
var mapsTbl = $('.table-widget', mapsElm);

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the player identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual player screen
         playersElm.hide();
         playerElm.show();
         weaponsElm.show();
         enemiesElm.show();
         mapsElm.show();
         $.mgr.requestPlayer(id);
      } else {

         // Show the players list screen
         mapsElm.hide();
         enemiesElm.hide();
         weaponsElm.hide();
         playerElm.hide();
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
      enemiesTbl.table();
      enemiesTbl.table('loading');
      mapsTbl.table();
      mapsTbl.table('loading');

      // Configure the request options
      var options = {
         url: 'services/players/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onPlayer, $.mgr),
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

      // Populate the table with player results
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
