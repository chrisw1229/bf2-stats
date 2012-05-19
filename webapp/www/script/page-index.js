// Handles all the controller logic for the live front page
$(function() {

// Register the page manager as a jQuery extension
$.extend({ mgr: {

}});

// Load the custom jQuery user interface components
$('.logger-widget').logger();
$('.olmap-widget').olmap({ baseUrl: 'http://tobe.name/codstats2/tiles', mapName: 'mp_uo_carentan' });

});

