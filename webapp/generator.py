
import os.path
from time import sleep

# The current directory is needed in the config file
current_dir = os.path.abspath(os.path.dirname(__file__))

READ_PATH = current_dir + '/logs/bf2_game_log.txt'
WRITE_PATH = current_dir + '/logs/temp.txt'

BUFFER = 0
DELAY = 1
TARGET = 0

read_file = None
write_file = None

def startup():
    global read_file
    global write_file

    try:
        read_file = open(READ_PATH, 'r')
    except IOError:
        raise Exception('Unable to open stats log file: ' + READ_PATH)
    try:
        write_file = open(WRITE_PATH, 'w', 1)
    except IOError:
        raise Exception('Unable to open stats log file: ' + WRITE_PATH)

def generate():
    global read_file
    global write_file
    last_tick = None
    count = 0

    running = True
    while running:
        line = read_file.readline().strip()
        if (len(line) > 0):

            # Read the next log line and get the tick time
            elements = line.split(';')
            tick = int(elements[0])

            # Check whether an artificial delay should be applied
            if last_tick != None and tick != last_tick:
                if BUFFER and count > BUFFER or tick > TARGET:
                    sleep(DELAY)

            # Output the log line
            print line
            write_file.write(line)
            write_file.write('\n')
            write_file.flush()

            last_tick = tick
            count += 1
        else:
            running = False

def shutdown():
    read_file.close()
    write_file.close()
 
# Start the web application server
if __name__ == '__main__':
    startup()
    generate()
    shutdown()
