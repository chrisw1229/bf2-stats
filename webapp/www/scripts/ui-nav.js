(function($, undefined) {

$.widget('ui.nav', {

   // Configure the default widget options
   options: {
      header: 'G-Day XII',
      footer: '08-25-2012',
      icon: 'ui-icon-triangle-1-e',
      menus: [
         { name: 'Achievements', tip: '', url: 'achievements.html' },
         { name: 'Awards', tip: '', url: 'awards.html' },
         { name: 'Games', tip: '', url: 'games.html' },
         { name: 'Kits', tip: '', url: 'kits.html' },
         { name: 'Leaderboard', tip: '', url: 'leaderboard.html' },
         { name: 'Maps', tip: '', url: 'maps.html' },
         { name: 'Matchups', tip: '', url: 'matchups.html' },
         { name: 'Players', tip: '', url: 'players.html' },
         { name: 'Vehicles', tip: '', url: 'vehicles.html' },
         { name: 'Weapons', tip: '', url: 'weapons.html' }
      ]
   },

   _create: function() {

      // Build the document model
      this.element.addClass('ui-nav');
      this.contentElm = $('<div class="ui-nav-content"/>').appendTo(this.element);
      this.logoElm = $('<div class="ui-nav-logo">LOGO</div>').appendTo(this.contentElm);

      // Build the menu header
      this.headerDiv = $('<h2 class="ui-helper-reset ui-widget-header ui-corner-top ui-nav-menu-header">'
            + this.options.header + '</h2>').appendTo(this.contentElm);

      // Build the menu item elements
      this.menusElm = $('<div class="ui-nav-menus"/>').appendTo(this.contentElm);
      for (var i = 0; i < this.options.menus.length; i++) {
         var menu = this.options.menus[i];
         var menuElm = $('<h3 class="ui-helper-reset ui-state-default ui-nav-menu"/>').appendTo(this.menusElm);
         $('<span class="ui-icon ' + this.options.icon + ' ui-nav-menu-icon"/>').appendTo(menuElm);
         $('<a class="ui-nav-menu-link" href="' + menu.url + '" title="' + menu.tip + '">'
               + menu.name + '</a>').appendTo(menuElm);
      }

      // Build the menu footer
      this.footerElm = $('<h4 class="ui-helper-reset ui-widget-header ui-corner-bottom ui-nav-menu-footer">'
            + this.options.footer + '</h4>').appendTo(this.contentElm);

      // Bind the event handlers
      this.menusElm.on('mouseenter', '.ui-nav-menu',
            function(e) { $(this).addClass('ui-state-hover'); });
      this.menusElm.on('mouseleave', '.ui-nav-menu',
            function(e) { $(this).removeClass('ui-state-hover'); });
   },

   destroy: function() {

      // Clear the event handlers
      this.menusElm.off('mouseenter mouseleave');

      // Destroy the document model
      this.contentElm.remove();
      this.element.removeClass('ui-nav')

      $.Widget.prototype.destroy.call(this);
   }

});

}(jQuery));
