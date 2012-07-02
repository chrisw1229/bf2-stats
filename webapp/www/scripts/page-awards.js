// Handles all the controller logic for the awards page
$(function() {

var awardsElm = $('.awards-content');
var awardElm = $('.award-content');

var tableElm = $('.table-widget').table();

// Register the page manager as a jQuery extension
$.extend({ mgr: {

   onHistory: function(e) {
      var id = e.getState('id');
      if (id) {
         awardsElm.hide();
         awardElm.show();
         $.mgr.requestAward(id);
      } else {
         awardElm.hide();
         awardsElm.show();
         $.mgr.requestAwards();
      }
   },

   requestAwards: function() {
      console.log('AWARDS');
   },

   requestAward: function(id) {
      tableElm.table('loading');

      // Configure the request options
      var options = {
         url: 'services/awards/' + id,
         dataType: 'json',
         success: $.proxy($.mgr.onAward, $.mgr),
         error: $.proxy($.mgr.onError, $.mgr)
      };

      // Fetch the content for the selected award
      $.ajax(options);
   },

   onAward: function(data) {
   
      // Update the header
      var headerElm = $('.common-header', awardElm);
      headerElm.text(data.name + ' Award');
      $('.award-desc', awardElm).text(data.desc);
      $('.award-notes', awardElm).text(data.notes);

      tableElm.table('setColumns', data.columns);
      tableElm.table('setRows', data.rows);
   },

   onError: function(request, status, error) {
   
   }

}});

// Callback when the URL fragment changes
$(window).on('hashchange', $.mgr.onHistory);

// Load the custom jQuery user interface components
$('.logger-widget').logger();
$('.common-nav').nav();

// Trigger the history event on initial page load
$(window).trigger('hashchange');

});
