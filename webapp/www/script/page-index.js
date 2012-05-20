// Handles all the controller logic for the live front page
$(function() {

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   // Indicates whether or not the test service should be used
   test: $.getUrlParam(location.href, 'test'),

   // Callback from the server when the game changes
   onGame: function(e) {
      // TODO
   },

   // Callback from the server when a player changes
   onPlayer: function(e) {
      // TODO
   },

   // Callback from the server when an event changes
   onEvent: function(e) {
      // TODO
   },

   // Callback from the server when map markers change
   onMap: function(e) {
      // TODO
   },

   // Callback from the server when a message should be displayed
   onLog: function(e) {
      // TODO
   }

}});

// Load the custom jQuery user interface components
$('.logger-widget').logger();
$('.olmap-widget').olmap({ baseUrl: 'http://tobe.name/codstats2/tiles', mapName: 'mp_uo_carentan' });

// Configure the network callbacks
$.service.baseUrl = ($.mgr.test ? 'test' : 'live');
$.service.params = ($.mgr.test ? { test: $.mgr.test } : { });
$($.service).on('game', $.mgr.onGame);
$($.service).on('player', $.mgr.onPlayer);
$($.service).on('event', $.mgr.onEvent);
$($.service).on('map', $.mgr.onMap);
$($.service).on('log', $.mgr.onLog);

// Start fetching data from the server
setTimeout(function() { $.service.refresh(); }, 2000);

});
