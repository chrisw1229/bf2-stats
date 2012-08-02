## Overview
The goal of this project is to output and subsequently parse log files for the game Battlefield 2 and generate a wide range of statistical web pages that describe the performance of each player.

The focus will be on creating a modern and polished user experience that provides interesting and entertaining information to players of the game. It will support a real-time mode for use during LAN party events, as well as a comprehensive static mode for post-game viewing. It will also include a custom game mod that will make it possible to extract additional statistics not available in the standard game. There is no interest at this time in supporting other games.

## Setup

### Game
* Copy the modded game files in the folder `bf2-server` into the corresponding directory structure of the BF2 
server installation. Currently, the modifications consist of only two files. The existing `__init__.py` file was modified just to include a new custom file. The `logger.py` is a new custom file that listens to various standard game events and writes out log entries to an external file.

* Make sure the new code has permission to write log files. By default, it attempts to write the log files to a sub-folder of the currently executing game mod. Typically the standard game mod will be used, so the logs folder should be created at `mods/bf2/logs`. If the server was installed in a restricted folder like `Program Files` under Windows, then you should go ahead and grant your user account full permission to the new logs folder.

* If everything is setup correctly, then upon running the dedicated server you should see a new file written to the logs folder created above.

### Web Application
* Make sure Python 2.7.x is installed and the [Cherrypy](http://www.cherrypy.org) web server package is installed.

* [Download](https://github.com/chrisw1229/bf2-stats/downloads) and extract map tiles for each game map to the `webapp/www/tiles` directory.

* Set the location of your game log file using the `webapp/application.conf` configuration file.

* Run the `webapp/application.py` file to start the web application.