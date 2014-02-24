import sys, socket, string, random, os, time, traceback
from threading import Thread

OUTPUT_DELAY = 1
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')
MAX_FILE_SIZE = 1048576

class file_io_bot(Thread):

   def __init__(self, io_buffer):
      Thread.__init__(self)
      self.running = True
      self.io_buffer = io_buffer

   def run(self):
     while self.running:
       if not os.path.exists(OUTPUT_DIRECTORY):
         os.makedirs(OUTPUT_DIRECTORY)

       try:
          # Pacman Move Queue
          if self.io_buffer.pacman_move_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'pacman_commands.txt')

            # Truncate files over max size
            if os.path.isfile(file_path) and (os.path.getsize(file_path) >= MAX_FILE_SIZE):
              print "Pac-Man Move Queue is oversized, truncating"
              f = open(file_path, 'w')
              f.truncate()
              f.close()

            # Write the data we have
            while self.io_buffer.pacman_move_queue:
              f = open(file_path, 'a')
              data = self.io_buffer.pacman_move_queue.pop()
              data = (data[:14] + '..') if len(data) > 18 else data
              f.write(data + "\n")
              f.close()
       except:
         print "Exception writing Pac-Man move queue: ", traceback.format_exc()

       try:
          # Ghost Move Queue
          if self.io_buffer.ghost_move_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'ghost_commands.txt')

            # Truncate files over max size
            if os.path.isfile(file_path) and (os.path.getsize(file_path) >= MAX_FILE_SIZE):
              print "Ghost Move Queue is oversized, truncating"
              f = open(file_path, 'w')
              f.truncate()
              f.close()

            # Write the data we have
            while self.io_buffer.ghost_move_queue:
              f = open(file_path, 'a')
              data = self.io_buffer.ghost_move_queue.pop()
              data = (data[:14] + '..') if len(data) > 18 else data
              f.write(data + "\n")
              f.close()
       except:
         print "Exception writing Ghost move queue: ", traceback.format_exc()
           
       try:
           # Pacman Score
          if self.io_buffer.pacman_score_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'pacman_score.txt')
            score = 0

            if os.path.isfile(file_path):
              f = open(file_path, 'r')
              score = int(f.readline().strip())
              f.close()

            while self.io_buffer.pacman_score_queue:
              score += self.io_buffer.pacman_score_queue.pop()

            f = open(file_path, 'w')
            f.write(str(score))
            f.close()
       except:
         print "Exception writing pacman score: ", traceback.format_exc()

       try:
          # Ghost Score
          if self.io_buffer.ghost_score_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'ghost_score.txt')
            score = 0

            if os.path.isfile(file_path):
              f = open(file_path, 'r')
              score = int(f.readline().strip())
              f.close()

            while self.io_buffer.ghost_score_queue:
              score += self.io_buffer.ghost_score_queue.pop()

            f = open(file_path, 'w')
            f.write(str(score))
            f.close()
       except:
         print "Exception writing ghost score: ", traceback.format_exc()

       time.sleep(OUTPUT_DELAY)


   def stop_running(self):
     self.running = False
     print "IO Bot set to shutdown"

