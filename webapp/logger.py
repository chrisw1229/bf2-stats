import time

def init():
   print 'LOGGER - INIT'

   # Build a path to the target log output file
   logFileName = 'logs/log.txt'
   print 'Writing log file: ', logFileName

   # Open the log file in line-buffered write mode
   logFile = None
   try:
      logFile = open(logFileName, 'w', 1)
   except IOError:
      print 'Unable to open log file: ', logFileName
      return

   for i in range(60):
      line = str(i).zfill(5) + ';AA;Test;11,22,33;test'
      print line

      logFile.write(line)
      logFile.write('\n')
      logFile.flush()
      time.sleep(1)
   logFile.close()

init()