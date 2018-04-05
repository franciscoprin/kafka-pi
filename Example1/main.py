from Example1.GraphThread import GraphThread

from Example1.Queue import Queue
from Example1.ConsumerThread import ConsumerThread
from Example1.ProducerThread import ProducerThread
import threading

points = Queue()
semaphore = threading.Semaphore(2)


producer = ProducerThread(10,points,semaphore)
consumer = ConsumerThread(1,points,semaphore)
graph = GraphThread(0.5,points,semaphore)


# Start will immediately call the run immediately inside of ProducerThread and ConsumerThread classes..
producer.start()
consumer.start()
graph.start()
producer.join()
consumer.join()
graph.join()

print ("Exiting Main Thread")

