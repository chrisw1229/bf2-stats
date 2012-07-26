(function($, undefined) {

$.widget('ui.olmap', {

   // Configure the default widget options
   options: {
      baseUrl: undefined,
      center: [8192, 8192],
      maxSize: 16384,
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
      this.overlays = {};
      this._addLineLayer('target', 'Targetting lines');
      this._addPointLayer('victim', 'Victims');
      this._addPointLayer('attacker', 'Attackers');
      this._addPointLayer('vehicle', 'Vehicles');
      this._addPointLayer('flag', 'Flags');

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
         this.tileLayer = this._updateTileLayer();
      }
   },

   addMarker: function(model) {
      if (model.type == 'KL') {
         this.addKill(model);
      } else if (model.type == 'VD') {
         this.addVehicle(model);
      }
   },

   // Adds the given victim marker to the map
   addKill: function(model) {
      this._addPoint('victim', model.victim);
      if (model.attacker) {
         this._addPoint('attacker', model.attacker);
         this._addLine('target', model);
      }
   },

   // Removes the given victim marker from the map
   removeKill: function(model) {
      this._removeFeature('victim', model.victim);
      if (model.attacker) {
         this._removeFeature('attacker', model.attacker);
         this._removeFeature('target', model);
      }
   },

   // Adds the given victim marker to the map
   addVehicle: function(model) {
      this._addPoint('vehicle', model.vehicle);
   },

   // Removes all the map markers
   clearMarkers: function() {
      for (var type in this.overlays) {
         var overlay = this.overlays[type];
         overlay.layer.removeAllFeatures();
         overlay.models = {};
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
   },

   // Creates a layer that displays targetting lines
   _addLineLayer: function(type, name) {

      // Configure the style for the layer
      var self = this;
      var styleOpts = new OpenLayers.Style({ strokeColor: '${color}',
         strokeWidth: '${width}'
      }, {
         context: {
            color: function(m) {
               var team = m.attributes.kteam;
               if (team == 'g') {
                  return '#FFB709';
               } else if (team == 'a' || team == 'r' || team == 'b') {
                  return '#64C461';
               }
               return '#ABABAB';
            },

            width: function(m) {
               return self.olmap.getZoom() + 1;
            }
         }
      });

      // Configure the target layer
      var layerOpts = {
         ratio: 2.0,
         rendererOptions: { yOrdering: true },
         styleMap: new OpenLayers.StyleMap({ 'default': styleOpts })
      }

      // Add the target layer to the map
      var layer = new OpenLayers.Layer.Vector('Kill lines', layerOpts);
      this.olmap.addLayer(layer);

      var overlay = {
         layer: layer,
         models: {}
      };
      this.overlays[type] = overlay;
   },

   // Creates a layer that displays marker graphics
   _addPointLayer: function(type, name) {

      // Configure the style for the layer
      var self = this;
      var styleOpts = new OpenLayers.Style({ cursor: 'pointer',
         externalGraphic: 'images/markers/' + type + '${size}.png',
         graphicWidth: '${size}', graphicHeight: '${size}'
      }, {
         context: {
            size: function(m) {

               // Use the current zoom level to select an image size otherwise
               var zoom = self.olmap.getZoom();
               return 8;
            }
         }
      });

      // Configure the marker layer
      var layerOpts = {
         ratio: 2.0,
         rendererOptions: { yOrdering: true },
         styleMap: new OpenLayers.StyleMap({ 'default': styleOpts })
      }

      // Add the marker layer to the map
      var layer = new OpenLayers.Layer.Vector(name, layerOpts);
      this.olmap.addLayer(layer);

      var overlay = {
         layer: layer,
         models: {}
      };
      this.overlays[type] = overlay;
   },

   _addPoint: function(type, model) {

      // Create a vector point for the model
      var point = new OpenLayers.Geometry.Point(model.x, model.y);
      var feature = new OpenLayers.Feature.Vector(point, model);

      // Add the feature to the associated layer
      var overlay = this.overlays[type];
      if (overlay) {
         overlay.layer.addFeatures(feature);
         overlay.models[model] = feature;
      }
   },

   _addLine: function(type, model) {

      // Create a vector point for the model
      var point1 = new OpenLayers.Geometry.Point(model.victim.x, model.victim.y);
      var point2 = new OpenLayers.Geometry.Point(model.attacker.x, model.attacker.y);
      var line = new OpenLayers.Geometry.LineString([point1, point2]);
      var feature = new OpenLayers.Feature.Vector(line, model);

      // Add the feature to the associated layer
      var overlay = this.overlays[type];
      if (overlay) {
         overlay.layer.addFeatures(feature);
         overlay.models[model] = feature;
      }
   },

   _removeFeature: function(type, model) {
      var overlay = this.overlays[type];
      if (overlay) {
         var feature = overlay.models[model];
         if (feature) {
            overlay.layer.removeFeatures(feature);
            delete overlay.models[model];
         }
      }
   }

});

}(jQuery));
