// Handles all the controller logic for the replay page
$(function() {

var headerElm = $('.header-container');
var playBtn = $('.play-button', headerElm).button(
      { icons: { primary: 'ui-icon-play' } });
var pauseBtn = $('.pause-button', headerElm).button(
      { icons: { primary: 'ui-icon-pause' } });
var stopBtn = $('.stop-button', headerElm).button(
      { icons: { primary: 'ui-icon-stop' } });
var sliderElm = $('.slider-widget', headerElm).slider();
var mapElm = $('.olmap-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the kit identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual kit screen
         $.mgr.requestGame(id);
      }
   },

   requestGame: function(id) {

      // Configure the request options
      var options = {
         url: 'services/replays/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onGame, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected kit
      $.ajax(options);
   },

   onGame: function(data) {
      $.mgr.game = data;

      // Update the header
      var headerElm = $('.common-header', headerElm);
      headerElm.text('Game - ' + data.map_name);

      // Update the map tiles based on the current game
      mapElm.olmap({ mapName: 'dalian_plant' });

      // Update the value range of the slider
      sliderElm.slider({ min: data.packets[0].tick,
            max: data.packets[data.packets.length - 1].tick, value: 0 });

      stopBtn.trigger('click');
   },

   onPlay: function(e) {
      $.mgr.playing = true;
      playBtn.hide();
      pauseBtn.show();

      $.mgr.displayTick(sliderElm.slider('value'));
      $.mgr.stepTick();
   },

   onPause: function(e) {
      $.mgr.playing = false;
      playBtn.show();
      pauseBtn.hide();
   },

   onStop: function(e) {
      $.mgr.playing = false;
      playBtn.show();
      pauseBtn.hide();

      var min = sliderElm.slider('option', 'min');
      sliderElm.slider('value', min);
      $.mgr.displayAll();
   },

   onSlideChange: function(e, ui) {
      $.mgr.displayTick(ui.value);
   },

   stepTick: function() {
      setTimeout(function() {
         if (!$.mgr.playing) {
            return;
         }
         var value = sliderElm.slider('value');
         var max = sliderElm.slider('option', 'max');
         if (value < max) {
            sliderElm.slider('value', value + 1);
            $.mgr.stepTick();
         }
      }, 100);
   },

   displayAll: function() {

      // Remove any previous markers
      mapElm.olmap('clearMarkers');

      // Add all the markers for the current game
      var packets = $.mgr.game.packets;
      for (var i = 0; i < packets.length; i++) {
         mapElm.olmap('addMarker', packets[i]);
      }
   },

   displayTick: function(tick) {

      // Remove any previous markers
      mapElm.olmap('clearMarkers');

      // Add all the markers for the selected tick
      var packets = $.mgr.game.packets;
      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.tick < tick) {
            continue;
         } else if (packet.tick == tick) {
            mapElm.olmap('addMarker', packet);
         } else if (packet.tick > tick) {
            break;
         }
      }
   }

}});

// Callback when the URL fragment changes
$(window).on('hashchange', $.mgr.onHistory);

// Callback when the playback buttons are clicked
playBtn.on('click', $.mgr.onPlay);
pauseBtn.on('click', $.mgr.onPause);
stopBtn.on('click', $.mgr.onStop);

// Callback when the slider value changes
sliderElm.on('slide', $.mgr.onSlideChange);
sliderElm.on('slidechange', $.mgr.onSlideChange);

// Trigger the history event on initial page load
$(window).trigger('hashchange');

});
