
import json
import os.path
import Queue
import threading
import urllib2

current_dir = os.path.abspath(os.path.dirname(__file__))

BASE_DIR = current_dir + '/__export/services'
BASE_URL = 'http://localhost/services'
THREADS = 25

def export():
    queue = Queue.Queue()

    _get_awards_urls(queue)
    _get_games_urls(queue)
    _get_kits_urls(queue)
    _get_leaderboard_urls(queue)
    _get_maps_urls(queue)
    _get_overview_urls(queue)
    _get_players_urls(queue)
    _get_teams_urls(queue)
    _get_vehicles_urls(queue)
    _get_weapons_urls(queue)

    _start_threads(queue)
    queue.join()

def _get_awards_urls(queue):
    index = _export_url('awards', 'index.json', True)
    for model in index:
        queue.put(('awards', model['id'] + '.json'))

def _get_games_urls(queue):
    index = _export_url('games', 'index.json', True)
    for model in index:
        queue.put(('games', model['id'] + '.json'))
        queue.put(('replays', model['id'] + '.json'))

def _get_kits_urls(queue):
    index = _export_url('kits', 'index.json', True)
    for model in index:
        queue.put(('kits', model['id'] + '.json'))

def _get_leaderboard_urls(queue):
    _export_url('leaderboard', 'index.json', True)

def _get_maps_urls(queue):
    index = _export_url('maps', 'index.json', True)
    for model in index:
        queue.put(('maps', model['id'] + '.json'))

def _get_overview_urls(queue):
    _export_url('overview', 'index.json', True)

def _get_players_urls(queue):
    index = _export_url('players', 'index.json', True)
    for model in index:
        base_dir = BASE_DIR + '/players/' +  model['id']
        if not os.path.exists(base_dir):
            os.makedirs(base_dir)

        queue.put(('players/' + model['id'], 'statistics.json'))
        queue.put(('players/' + model['id'], 'enemies.json'))
        queue.put(('players/' + model['id'], 'kits.json'))
        queue.put(('players/' + model['id'], 'maps.json'))
        queue.put(('players/' + model['id'], 'teams.json'))
        queue.put(('players/' + model['id'], 'vehicles.json'))
        queue.put(('players/' + model['id'], 'weapons.json'))

def _get_teams_urls(queue):
    index = _export_url('teams', 'index.json', True)
    for model in index:
        queue.put(('teams', model['id'] + '.json'))

def _get_vehicles_urls(queue):
    index = _export_url('vehicles', 'index.json', True)
    for model in index:
        queue.put(('vehicles', model['id'] + '.json'))

def _get_weapons_urls(queue):
    index = _export_url('weapons', 'index.json', True)
    for model in index:
        queue.put(('weapons', model['id'] + '.json'))

def _start_threads(queue):
    for i in range(THREADS):
        thread = threading.Thread(target=_run_thread, args=[queue])
        thread.daemon = True
        thread.start()

def _run_thread(queue):
    while True:
        service_id, file_id = queue.get()
        _export_url(service_id, file_id)
        queue.task_done()

def _export_url(service_id, file_id, parse=False):
    base_dir = BASE_DIR + '/' + service_id
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    file_url = BASE_URL + '/' + service_id + '/' + file_id
    print 'Fetching: ' + file_url
    url = urllib2.urlopen(file_url)
    content = url.read()

    file = open(base_dir + '/' + file_id, 'w')
    file.write(content)
    file.close()

    if parse:
        tuple = json.loads(content)
        return tuple

# Start the main application
if __name__ == '__main__':
    export()
 