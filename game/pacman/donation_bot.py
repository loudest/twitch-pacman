from threading import Thread

OUTPUT_DELAY = 1
UNITS_OF_WORK = 200

class donation_bot(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.running = True
    self.uow = UNITS_OF_WORK

  def flush(self):
    return
  
  def run(self):
    while (self.running and self.uow > 0):
      self.uow -= 1
      self.flush()
      time.sleep(OUTPUT_DELAY)

  def stop_running(self):
    self.running = False
    print "Donation Bot set to shutdown"
