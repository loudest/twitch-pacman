from threading import Thread

class donation_bot(Thread):
  def __init__(self):
    Thread.__init__(self)
    self.running = True

  def stop_running(self):
    self.running = False
    print "Donation Bot set to shutdown"
