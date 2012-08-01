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

   FRAME_RATE: 50,
   MARKER_TIME: 5000,

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

      // Update the header
      var headerElm = $('.common-header', headerElm);
      headerElm.text('Game - ' + data.map_name);

      // Update the map tiles based on the current game
      mapElm.olmap({ mapName: 'dalian_plant' });

      // Pre-process the packets to prepare for plotting
      var controlPoints = [];
      var packets = {};
      for (var i = 0; i < data.packets.length; i++) {
         var packet = data.packets[i];
         if (packet.type == 'CP') {
            controlPoints.push(packet);
         } else {
            if (packets[packet.tick] == undefined) {
               packets[packet.tick] = [];
            }
            packets[packet.tick].push(packet);
         }
      }
      $.mgr.controlPoints = controlPoints;
      $.mgr.packets = packets;

      // Update the value range of the slider
      sliderElm.slider({ min: data.packets[0].tick,
            max: data.packets[data.packets.length - 1].tick, value: 0 });

      // Simulate a stop click to show all packets at once
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

      $.mgr.lastTick = undefined;
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
      }, $.mgr.FRAME_RATE);
   },

   displayAll: function() {

      // Remove any previous markers
      mapElm.olmap('clearMarkers');

      // Get the final state of the control points
      var max = sliderElm.slider('option', 'max');
      var controlPoints = $.mgr.getControlPoints(max);
      mapElm.olmap('addPackets', controlPoints);

      // Add all the markers for the current game
      var packets = $.mgr.packets;
      for (var tick in $.mgr.packets) {
         mapElm.olmap('addPackets', $.mgr.packets[tick]);
      }
   },

   displayTick: function(tick) {
      oldTick = $.mgr.lastTick;
      $.mgr.lastTick = tick;
      if (oldTick == tick) {
         return;
      }

      // Check whether an incremental update can be used
      if (oldTick == tick - 1) {
         $.mgr.displayTickDiff(tick);
         return;
      }

      // Remove any previous markers
      mapElm.olmap('clearMarkers');

      // Add the final state of the control points
      
      mapElm.olmap('addPackets', $.mgr.getControlPoints(tick));

      // Add all the markers for the selected tick
      mapElm.olmap('addPackets', $.mgr.packets[tick]);
   },

   displayTickDiff: function(tick) {
   
      // Update the state of the control points
      mapElm.olmap('clearControlPoints');
      mapElm.olmap('addPackets', $.mgr.getControlPoints(tick));

      // Clear any expired packets
      var offset = tick - Math.floor($.mgr.MARKER_TIME / $.mgr.FRAME_RATE);
      mapElm.olmap('removePackets', $.mgr.packets[offset]);

      // Add packets for the current tick
      mapElm.olmap('addPackets', $.mgr.packets[tick]);
   },

   getControlPoints: function(tick) {
      var states = {};
      for (var i = 0; i < $.mgr.controlPoints.length; i++) {
         var packet = $.mgr.controlPoints[i];
         if (packet.tick <= tick) {
            states[packet.control_point.id] = packet;
         } else if (packet.tick > tick) {
            break;
         }
      }
      var controlPoints = [];
      for (var id in states) {
         controlPoints.push(states[id]);
      }
      return controlPoints;
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
