// Handles all the controller logic for the games page
$(function() {

var gamesElm = $('.games-content');
var listElm = $('.list-widget');

var gameElm = $('.game-content');
var replayBtn = $('.replay-button');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the game identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual game screen
         gamesElm.hide();
         gameElm.show();
         $.mgr.requestGame(id);
      } else {

         // Show the games list screen
         gameElm.hide();
         gamesElm.show();
         $.mgr.requestGames();
      }
   },

   requestGames: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/games/index.json',
         dataType: 'json',
         success: $.proxy($.mgr.onGames, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected game
      $.ajax(options);
   },

   requestGame: function(id) {

      // Display the loading indicator
      tableElm.table({ showAll: true });
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/games/' + id + '.json',
         dataType: 'json',
         success: $.proxy($.mgr.onGame, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected game
      $.ajax(options);
   },

   onGames: function(data) {

      // Update the header
      var headerElm = $('.common-header', gamesElm);
      headerElm.text('Games (' + data.length + ')');

      // Populate the list with games
      listElm.list('setRows', data);
   },

   onGame: function(data) {

      // Update the header
      var headerElm = $('.common-header-title', gameElm);
      headerElm.text(data.name);

      // Update the replay button link
      $('.replay-button').button({ icons: { secondary: 'ui-icon-extlink' } })
            .attr('href', 'replays.html#id=' + data.id);

      // Populate the table with game results
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
