(function($, undefined) {

$.widget('ui.olmap', {

   // Configure the default widget options
   options: {
      baseUrl: undefined,
      center: [2048, 2048],
      maxMarkers: 25,
      maxSize: 4096,
      maxTile: 256,
      maxZoom: 7,
      mapName: undefined,
      zoom: 2
   },

   _create: function() {
      this.element.addClass('ui-olmap');

      // Setup the map container
      this.mapElm = $('<div class="ui-olmap-container"/>').appendTo(this.element);
 
      // Create the map controls
      var keyCtrl = new OpenLayers.Control.KeyboardDefaults();
      var navCtrl = new OpenLayers.Control.Navigation({
         dragPanOptions: { enableKinetic: true }
      });
      var panCtrl = new OpenLayers.Control.PanPanel({
         slideFactor: 125
      });
      var zoomCtrl = new OpenLayers.Control.ZoomPanel();

      // Create the actual map component
      var mapOpts = {
         controls: [keyCtrl, navCtrl, panCtrl, zoomCtrl],
         theme: null
      };
      this.olmap = new OpenLayers.Map(this.mapElm[0], mapOpts);

      // Create the map layers
      this.tileLayer = this._updateTileLayer();

      // Set control tool tips
      var panElm = $('.olControlPanPanel', this.mapElm); 
      $('.olControlPanNorthItemActive', panElm).attr('title', 'Pan up');
      $('.olControlPanSouthItemActive', panElm).attr('title', 'Pan down');
      $('.olControlPanEastItemActive', panElm).attr('title', 'Pan right');
      $('.olControlPanWestItemActive', panElm).attr('title', 'Pan left');
      var zoomElm = $('.olControlZoomPanel', this.mapElm);
      $('.olControlZoomInItemActive', zoomElm).attr('title', 'Zoom in');
      $('.olControlZoomToMaxExtentItemActive', zoomElm).attr('title', 'Zoom to fit');
      $('.olControlZoomOutItemActive', zoomElm).attr('title', 'Zoom out');
   },

   destroy: function() {
      this.olmap.destroy();
      this.mapElm.remove();
      this.element.removeClass('ui-olmap');

      $.Widget.prototype.destroy.call(this);
   },

   _setOption: function(key, value) {
      $.Widget.prototype._setOption.apply(this, arguments);

      // Update the map tiles if requested
      if (key === 'mapName') {
         this.tileLayer = this._updateTileLayer(value);
      }
   },

   // Enables or disables the map controls
   _setEnabled: function(enabled) {

      // Only allow mouse interaction when tiles are loaded
      var display = enabled ? 'block' : 'none';
      $('.olControlPanPanel', this.mapElm).css('display', display);
      $('.olControlZoomPanel', this.mapElm).css('display', display);
      for (var i = 0; i < this.olmap.controls.length; i++) {
         var control = this.olmap.controls[i];
         if (enabled) {
            control.activate();
         } else {
            control.deactivate();
         }
      }

      // Adjust the map appearance
      if (enabled) {
         this.mapElm.addClass('ui-olmap-enabled');

         // Set the default pan and zoom values
         var lon = this.options.center[0];
         var lat = this.options.center[1];
         this.olmap.setCenter(new OpenLayers.LonLat(lon, lat), this.options.zoom);
      } else {
         this.mapElm.removeClass('ui-olmap-enabled');
      }
   },

   _updateTileLayer: function() {

      // Remove the old tile layer if the map name actually changed
      if (this.tileLayer && this.tileLayer.mapName != this.options.mapName) {
         this.olmap.removeLayer(this.tileLayer);
      }

      // Only create the layer if a map name was given
      if (this.options.mapName === undefined) {
         this._setEnabled(false);
         return;
      }

      // Configure the tile layer
      var layerOpts = {
         maxExtent: new OpenLayers.Bounds(0, 0, this.options.maxSize, this.options.maxSize),
         maxResolution: (this.options.maxSize / this.options.maxTile),
         numZoomLevels: this.options.maxZoom,
         transitionEffect: 'resize'
      };

      // Build the map tile query URL
      var tileUrl = this.options.baseUrl ? this.options.baseUrl + '/' : 'tiles/';
      tileUrl += this.options.mapName + '/${z}/${x}_${y}.jpg';

      // Create the tile layer to the map
      var layer = new OpenLayers.Layer.XYZ('Tiles', tileUrl, layerOpts);
      layer.mapName = this.options.mapName;
      this.olmap.addLayer(layer);

      // Enable the map controls if tiles are configured
      this._setEnabled(this.options.mapName != undefined);
      return layer;
   }

});

}(jQuery));
