from Raspberry_Producer.ProducerThread import ProducerThread
from Raspberry_Producer.Button import Button
import threading

print("Here we go! Press CTRL+Z to exit")

semaphore = threading.Semaphore(1)

producer = ProducerThread(semaphore)
button = Button(semaphore)

# The start method bellow will call the the run methods inside of ProducerThread and Button classes.
producer.start()
button.start()
producer.join()
button.join()

print ("Exiting Main Thread")