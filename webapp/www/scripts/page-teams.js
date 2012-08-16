// Handles all the controller logic for the teams page
$(function() {

var teamsElm = $('.teams-content');
var listElm = $('.list-widget');

var teamElm = $('.team-content');
var tableElm = $('.table-widget');

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {

      // Get the team identifier if available
      var id = e.getState('id');
      if (id) {

         // Show the individual team screen
         teamsElm.hide();
         teamElm.show();
         $.mgr.requestTeam(id);
      } else {

         // Show the teams list screen
         teamElm.hide();
         teamsElm.show();
         $.mgr.requestTeams();
      }
   },

   requestTeams: function() {

      // Display the loading indicator
      listElm.list();
      listElm.list('loading');

      // Configure the request options
      var options = {
         url: 'services/teams',
         dataType: 'json',
         success: $.proxy($.mgr.onTeams, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected team
      $.ajax(options);
   },

   requestTeam: function(id) {

      // Display the loading indicator
      tableElm.table({ showAll: true });
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/teams/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onTeam, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected team
      $.ajax(options);
   },

   onTeams: function(data) {

      // Update the header
      var headerElm = $('.common-header', teamsElm);
      headerElm.text('Teams (' + data.length + ')');

      // Populate the list with teams
      listElm.list('setRows', data);
   },

   onTeam: function(data) {

      // Update the header
      var headerElm = $('.common-header', teamElm);
      headerElm.text('Team - ' + data.name);

      // Populate the table with team results
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
