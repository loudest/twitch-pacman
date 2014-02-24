import sys, socket, string, random, os, time, traceback, logging
from threading import Thread

OUTPUT_DELAY = 1
OUTPUT_DIRECTORY = os.path.join(os.path.dirname(__file__), 'output')
MAX_FILE_SIZE = 1048576
UNITS_OF_WORK = 200

class file_io_bot(Thread):

   def __init__(self, io_buffer):
      Thread.__init__(self)
      self.running = True
      self.io_buffer = io_buffer
      self.uow = UNITS_OF_WORK
      self.logger = logging.getLogger('pacman')
      

   def run(self):
     self.logger.info("File IO bot starting, UOW is " + str(self.uow))

     while (self.running and self.uow > 0):
       self.uow -= 1

       try:
         if not os.path.exists(OUTPUT_DIRECTORY):
           os.makedirs(OUTPUT_DIRECTORY)
       except:
         self.logger.error("Exception creating directory: " + traceback.format_exc())

       try:
          # Pacman Move Queue
          if self.io_buffer.pacman_move_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'pacman_commands.txt')

            # Truncate files over max size
            if os.path.isfile(file_path) and (os.path.getsize(file_path) >= MAX_FILE_SIZE):
              self.logger.info("Pac-Man Move Queue is oversized, truncating")
              f = open(file_path, 'w')
              f.truncate()
              f.close()

            # Write the data we have
            while self.io_buffer.pacman_move_queue:
              f = open(file_path, 'a')
              data = self.io_buffer.pacman_move_queue.pop()
              data = (data[:16] + '..') if len(data) > 18 else data
              f.write(data + "\n")
              f.close()
       except:
         self.logger.error("Exception writing Pac-Man move queue: " + traceback.format_exc())

       try:
          # Ghost Move Queue
          if self.io_buffer.ghost_move_queue:
            file_path = os.path.join(OUTPUT_DIRECTORY, 'ghost_commands.txt')

            # Truncate files over max size
            if os.path.isfile(file_path) and (os.path.getsize(file_path) >= MAX_FILE_SIZE):
              self.logger.info("Ghost Move Queue is oversized, truncating")
              f = open(file_path, 'w')
              f.truncate()
              f.close()

            # Write the data we have
            while self.io_buffer.ghost_move_queue:
              f = open(file_path, 'a')
              data = self.io_buffer.ghost_move_queue.pop()
              data = (data[:16] + '..') if len(data) > 18 else data
              f.write(data + "\n")
              f.close()
       except:
         self.logger.error("Exception writing Ghost move queue: " + traceback.format_exc())
           
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
         self.logger.error("Exception writing pacman score: " + traceback.format_exc())

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
         self.logger.error("Exception writing ghost score: " + traceback.format_exc())

       time.sleep(OUTPUT_DELAY)

     self.logger.info("File IO Bot stopping, UOW is " + str(self.uow))

   def stop_running(self):
     self.running = False
     self.logger.info("IO Bot set to shutdown")

