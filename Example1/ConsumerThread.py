import threading
import time
from Example1.Consumer import Consumer

exitFlag = 0

class ConsumerThread (threading.Thread):
   def __init__(self, delay,points,semaphore):
      threading.Thread.__init__(self)
      self.delay = delay
      self.points = points
      self.semaphore = semaphore

   def run(self):
      consumer = Consumer()
      # consumer.setPort(9092)
      # consumer.setIP("52.186.81.99")
      consumer.startConnection()
      self.points.consumerTime = time.time()
      while True:
         self.semaphore.acquire()
         consumer.getMessage(self.points)
         self.semaphore.release()






