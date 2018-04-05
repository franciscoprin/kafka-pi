import threading
import time
from Example1.Producer import Producer
from Example1.Point import Point
import math

class ProducerThread(threading.Thread):
    def __init__(self, delay, points, semaphore):
        threading.Thread.__init__(self)
        self.points = points
        self.delay = delay
        self.semaphore = semaphore

    def run(self):
        producer = Producer()
        # producer.setPort(9092)
        # producer.setIP("52.186.81.99")

        producer.startConnection()
        self.points.producerTime = time.time()
        self.semaphore.acquire()
        for x in range(0, 100):
            print("PRODUCER: Sending message....")
            producer.sendMessage(Point(5 * x, 10 * math.sin(5 * x + 10) + 40))
            if (x % 10 == 0):
                self.semaphore.release()
                time.sleep(self.delay)
                self.semaphore.acquire()
