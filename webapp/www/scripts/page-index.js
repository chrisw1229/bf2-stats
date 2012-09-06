// Handles all the controller logic for the index page
$(function() {

var statsElm = $('.stats-list');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   requestOverview: function() {
      statsElm.empty();

      // Configure the request options
      var options = {
         url: 'services/overview/index.json',
         dataType: 'json',
         success: $.proxy($.mgr.onOverview, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content
      $.ajax(options);
   },

   onOverview: function(data) {
      $.mgr._addStat('Total Score', data.score);
      $.mgr._addStat('Total Kills', data.kills);
      $.mgr._addStat('Total Deaths', data.deaths);
      $.mgr._addStat('Concurrent Players', data.players);
      $.mgr._addStat('Server Log Entries', data.lines);
      $.mgr._addStat('Cock Dogs Eaten', 377);
   },

   onError: function(request, status, error) {

   },

   _addStat: function(key, value) {
      value = value.toString();
      var pos = value.length;
      for (var i = value.length - 3; i > 0; i-=3) {
         value = value.substring(0, i) + ',' + value.substring(i, pos);
      }

      $('<li><span class="stat-label">' + key + '</span><span class="stat-value">'
            + value + '</span></li>').appendTo(statsElm);
   }

}});

// Load the custom jQuery user interface components
$('.common-nav').nav();

$.mgr.requestOverview();

});
