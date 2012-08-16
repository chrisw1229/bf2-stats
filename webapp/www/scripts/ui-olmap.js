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
      var layerCtrl = new OpenLayers.Control.LayerSwitcher({
         'ascending': false
      });
      var navCtrl = new OpenLayers.Control.Navigation({
         dragPanOptions: { enableKinetic: true }
      });
      var panCtrl = new OpenLayers.Control.PanPanel({
         slideFactor: 125
      });
      var zoomCtrl = new OpenLayers.Control.ZoomPanel();

      // Create the actual map component
      OpenLayers.ImgPath = '../images/';
      var mapOpts = {
         controls: [keyCtrl, layerCtrl, navCtrl, panCtrl, zoomCtrl],
         theme: null
      };
      this.olmap = new OpenLayers.Map(this.mapElm[0], mapOpts);

      // Create the map layers
      this.tileLayer = this._updateTileLayer();
      this.overlays = {};
      this._addPointLayer('control-point', 'Flags', 20,
            function(m) { return 'control-point-'
                  + (m.attributes.team_id ? m.attributes.team_id : 'none'); });
      this._addPointLayer('vehicle', 'Vehicles', 12);
      this._addLineLayer('target', 'Target lines');
      this._addPointLayer('victim', 'Victims', 8);
      this._addPointLayer('attacker', 'Attackers', 8);

      // Add the hover control after the feature layers are created
      this.hoverCtrl = this._createHoverControl();
      this.olmap.addControl(this.hoverCtrl);
      if (this.enabled) {
         this.hoverCtrl.activate();
      }

      // Apply fixes to the layer control
      var layerElm = $('.olControlLayerSwitcher', this.mapElm);
      $('.layersDiv', layerElm).addClass('ui-widget-content ui-corner-all');
      $('.maximizeDiv', layerElm).attr('title', 'Layers');
      $('.dataLbl', layerElm).html('Layers');

      // Apply fixes to the pan control
      var panElm = $('.olControlPanPanel', this.mapElm); 
      $('.olControlPanNorthItemActive', panElm).attr('title', 'Pan up');
      $('.olControlPanSouthItemActive', panElm).attr('title', 'Pan down');
      $('.olControlPanEastItemActive', panElm).attr('title', 'Pan right');
      $('.olControlPanWestItemActive', panElm).attr('title', 'Pan left');

      // Apply fixes to the zoom control
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

   // Adds the given control point marker to the map
   addControlPoint: function(controlPoint) {
      this._addPoint('control-point', controlPoint);
   },

   // Adds the given victim and attacker markers to the map
   addKill: function(kill, victim, attacker) {
      this._addPoint('victim', victim);
      if (attacker) {
         this._addPoint('attacker', attacker);
         this._addLine('target', kill);
      }
   },

   addPackets: function(packets) {
      if (packets == undefined) {
         return;
      }
      packets = $.isArray(packets) ? packets : [packets];

      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.type == 'KL') {
            this.addKill(packet, packet.victim, packet.attacker);
         } else if (packet.type == 'VD') {
            this.addVehicle(packet.vehicle);
         } else if (packet.type == 'CP') {
            this.addControlPoint(packet.control_point);
         }
      }
   },

   // Adds the given victim marker to the map
   addVehicle: function(vehicle) {
      this._addPoint('vehicle', vehicle);
   },

   // Removes all the map markers
   clearMarkers: function() {
      for (var type in this.overlays) {
         var overlay = this.overlays[type];
         overlay.layer.removeAllFeatures();
         overlay.models = {};
      }
   },

   // Removes all the control point markers
   clearControlPoints: function() {
      var overlay = this.overlays['control-point'];
      overlay.layer.removeAllFeatures();
      overlay.models = {};
   },

   // Removes the given control point marker from the map
   removeControlPoint: function(controlPoint) {
      this._removeFeature('control-point', controlPoint);
   },

   // Removes the given victim and attacker markers from the map
   removeKill: function(kill, victim, attacker) {
      this._removeFeature('victim', victim);
      if (attacker) {
         this._removeFeature('attacker', attacker);
         this._removeFeature('target', kill);
      }
   },

   // Removes the given vehicle marker from the map
   removeVehicle: function(vehicle) {
      this._removeFeature('vehicle', vehicle);
   },

   removePackets: function(packets) {
      if (packets == undefined) {
         return;
      }
      packets = $.isArray(packets) ? packets : [packets];

      for (var i = 0; i < packets.length; i++) {
         var packet = packets[i];
         if (packet.type == 'KL') {
            this.removeKill(packet, packet.victim, packet.attacker);
         } else if (packet.type == 'VD') {
            this.removeVehicle(packet.vehicle);
         } else if (packet.type == 'CP') {
            this.removeControlPoint(packet.control_point);
         }
      }
   },

   // Enables or disables the map controls
   _setEnabled: function(enabled) {
      this.enabled = enabled;

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
      displayInLayerSwitcher: false,
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
               var team = m.attributes.attacker.team_id;
               if (m.attributes.__selected__) {
                  return '#FFFFFF';
               } else if (team == 'us') {
                  return '#44D5FF';
               } else if (team == 'ch') {
                  return '#FFB7B4';
               } else if (team == 'mec') {
                  return '#FFD191';
               } else if (team == 'eu') {
                  return '#819DFF';
               }
               return '#C8C8C8';
            },

            width: function(m) {
               var width = self.olmap.getZoom() < 3 ? 1 : 2;
               if (m.attributes.__selected__) {
                  width += width;
               }
               return width;
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
      var layer = new OpenLayers.Layer.Vector(name, layerOpts);
      this.olmap.addLayer(layer);

      var overlay = {
         layer: layer,
         models: {}
      };
      this.overlays[type] = overlay;
   },

   // Creates a layer that displays marker graphics
   _addPointLayer: function(layerType, name, baseSize, typeFunc) {
      if (typeFunc == undefined) {
         typeFunc = function(m) { return layerType; };
      }

      // Configure the style for the layer
      var self = this;
      var styleOpts = new OpenLayers.Style({ cursor: 'pointer',
         externalGraphic: 'images/markers/${zoom}/${type}.png',
         graphicWidth: '${size}', graphicHeight: '${size}'
      }, {
         context: {

            size: function(m) {
               return baseSize + (2 * self.olmap.getZoom());
            },

            type: typeFunc,

            zoom: function(m) {
               return self.olmap.getZoom();
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
      this.overlays[layerType] = overlay;
   },

   _addPoint: function(type, model) {

      // Create a vector point for the model
      var point = new OpenLayers.Geometry.Point(model.x, model.y);
      var feature = new OpenLayers.Feature.Vector(point, model);

      // Add the feature to the associated layer
      this._addFeature(type, model, feature);
   },

   _addLine: function(type, model) {

      // Create a vector point for the model
      var point1 = new OpenLayers.Geometry.Point(model.victim.x, model.victim.y);
      var point2 = new OpenLayers.Geometry.Point(model.attacker.x, model.attacker.y);
      var line = new OpenLayers.Geometry.LineString([point1, point2]);
      var feature = new OpenLayers.Feature.Vector(line, model);

      // Add the feature to the associated layer
      this._addFeature(type, model, feature);
   },

   _addFeature: function(type, model, feature) {

      // Attempt to get the overlay for the feature type
      var overlay = this.overlays[type];
      if (overlay) {

         // Add the feature to the layer
         overlay.layer.addFeatures(feature);

         // Map the model to the feature using a unique hash code
         if (model.__hash__ == undefined) {
            this._hasher = this._hasher ? this._hasher : 0;
            model.__hash__ = ++this._hasher;
            feature.attributes.__hash__ = model.__hash__;
         }
         overlay.models[model.__hash__] = feature;
      }
   },

   _removeFeature: function(type, model) {

      // Attempt to get the overlay for the feature type
      var overlay = this.overlays[type];
      if (overlay) {

         // Get the feature associated with the given model
         if (model && model.__hash__) {
            var feature = overlay.models[model.__hash__];
            if (feature) {

               // Delete the feature from the layer
               overlay.layer.removeFeatures(feature);
               delete overlay.models[model.__hash__];

               // Hide the hover info if the feaure was selected
               if (this.hoverCtrl.selected) {
                  this.hoverCtrl.outFeature(feature);
               }
            }
         }
      }
   },

   _getKill: function(model) {
      var hash = model.__hash__;
      var models = this.overlays['target'].models;
      for (key in models) {
         var kill = models[key].attributes;
         if (kill.__hash__ == hash
               || (kill.victim && kill.victim.__hash__ == hash)
               || (kill.attacker && kill.attacker.__hash__ == hash)) {
            return kill;
         }
      }
   },

   _createHoverControl: function() {
      var self = this;
      OpenLayers.Control.Hover = OpenLayers.Class(OpenLayers.Control, {                

         initialize: function(options) {
            OpenLayers.Control.prototype.initialize.apply(this, arguments); 

            var hoverLayers = [
               self.overlays['attacker'].layer,
               self.overlays['target'].layer,
               self.overlays['vehicle'].layer,
               self.overlays['victim'].layer
            ];
            this.layer = new OpenLayers.Layer.Vector.RootContainer(
                  this.id + '_container', { layers: hoverLayers, ratio: 2.0 });
            this.callbacks = {
               over: this.overFeature,
               out: this.outFeature
            };
            this.handlers = {
               feature: new OpenLayers.Handler.Feature(this, this.layer,
                     this.callbacks)
            };
            this.dialogElm = $('.ui-olmap-dialog', self.element);
         },

         destroy: function() {
            OpenLayers.Control.prototype.destroy.apply(this, arguments);

            this.layer.destroy();
         },

         activate: function () {
            if (!this.active) {
               this.map.addLayer(this.layer);
               this.handlers.feature.activate();
            }
            return OpenLayers.Control.prototype.activate.apply(this, arguments);
         },

         deactivate: function () {
            if (this.active) {
               this.handlers.feature.deactivate();
               this.map.removeLayer(this.layer);
            }
            return OpenLayers.Control.prototype.deactivate.apply(this, arguments);
         },

         overFeature: function(feature) {
            var kill = $.proxy(self._getKill, self)(feature.attributes);
            var attacker = kill ? kill.attacker : undefined;
            var weapon = attacker ? attacker.weapon : undefined;
            var victim = kill ? kill.victim : feature.attributes;

            var contentElm = $('.ui-olmap-dialog-content', this.dialogElm);
            var attackerElm = $('.ui-olmap-dialog-attacker', contentElm);
            var weaponElm = $('.ui-olmap-dialog-weapon', contentElm);
            var victimElm = $('.ui-olmap-dialog-victim', contentElm);

            if (attacker) {
               contentElm.attr('class', 'ui-olmap-dialog-content'
                     + ' ui-olmap-dialog-team-' + attacker.team_id);

               attackerElm.text(attacker.name);
               attackerElm.show();

               weaponElm.text('[' + (weapon ? weapon : '?') + ']');
               weaponElm.show();

               victimElm.text(victim.name);
            } else {
               contentElm.attr('class', 'ui-olmap-dialog-content'
                     + ' ui-olmap-dialog-team-'
                     + (victim.team_id ? victim.team_id : 'none'));

               attackerElm.text('');
               attackerElm.hide();
               weaponElm.text('');
               weaponElm.hide();

               var victimMsg;
               if (victim.suicide) {
                  victimMsg = ' suicided.';
               } else if (victim.type) {
                  victimMsg = ' was destroyed.';
               } else {
                  victimMsg = ' died.';
               }
               victimElm.text(victim.name + victimMsg);
            }

            var maxW = self.element.width();
            this.dialogElm.css('left',
                  Math.round((maxW - this.dialogElm.width()) / 2));
            this.dialogElm.show();

            if (this.selected) {
               this.selected.__selected__ = undefined;
            }
            this.selected = kill;
            if (this.selected) {
               this.selected.__selected__ = true;
            }
            self.overlays['target'].layer.redraw();
         },

         outFeature: function(feature) {
            this.dialogElm.hide();

            if (this.selected) {
               this.selected.__selected__ = undefined;
               this.selected = undefined;
               self.overlays['target'].layer.redraw();
            }
         },

         setMap: function(map) {
            this.handlers.feature.setMap(map);

            OpenLayers.Control.prototype.setMap.apply(this, arguments);
         },

         resize: function() {
            this.dialogElm.hide();
         },

         CLASS_NAME: 'OpenLayers.Control.Hover'
      });
      return new OpenLayers.Control.Hover();
   }

});

}(jQuery));
