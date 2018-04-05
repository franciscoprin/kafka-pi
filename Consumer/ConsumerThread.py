import threading
import time
from Consumer.Consumer import Consumer


class ConsumerThread (threading.Thread):
   def __init__(self, delay,points,semaphore):
      threading.Thread.__init__(self)
      self.delay = delay
      self.points = points
      self.semaphore = semaphore

   def run(self):
      consumer = Consumer()
      # consumer.setPort(9092)
      # consumer.setIP("10.0.0.63")
      consumer.startConnection()
      
      self.points.consumerTime = time.time()
      while True:
         # self.semaphore.acquire()
         consumer.getMessage(self.points)
         # self.semaphore.release()


# consumer.seek(0, 0):  to start reading from the beginning of the queue.
# consumer.seek(0, 1): to start reading from current offset.
# consumer.seek(0, 2): to skip all the pending messages and start reading only new messages



