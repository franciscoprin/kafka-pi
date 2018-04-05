from Consumer.GraphThread import GraphThread
from Consumer.Queue import Queue
from Consumer.ConsumerThread import ConsumerThread
import threading

points = Queue()
semaphore = threading.Semaphore(1)
consumer = ConsumerThread(1,points,semaphore)
graph = GraphThread(0.5,points,semaphore)


# Start will immediately call the run immediately inside of ProducerThread and ConsumerThread classes..
consumer.start()
# graph.start()
consumer.join()
# graph.join()

print ("Exiting Main Thread")

