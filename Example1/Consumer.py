from kafka import KafkaClient
from kafka import KafkaConsumer
from Example1.Point import Point
import json
import time

class Consumer:
    def __init__(self):
        self.port = 9092
        self.ID = 'localhost'
        self.topic = 'test'
        self.group = None
        # the object that it is introduced should have a kafkaTime variable. If one of the objects does not have time,
        # would be ask the user to introduce a offset.
            # You need to find the lates offset.
            #
            # The user should decide if want to consume data from
                # Latest
                    # auto_offset_reset='latest'
                # specific offset.
                    # How I do this.
                # Specific time
                    # Count odd years??
                    # if a day is introduced you should convert that day in milliseconds, take in accoud
                    # after convert in milliseconds implet the funtion bellow.
                # Several seconds in the past

    def getLastestOffset(self):
        idPlusPort = self.ID+":" + str(self.port)
        kafka = KafkaClient(idPlusPort)
        # self.consumer = SimpleConsumer(kafka, "myGroup", self.topic)
        consumer =KafkaConsumer(self.topic,
                         group_id=self.group,
                         bootstrap_servers=[idPlusPort])
        consumer.poll()
        return(consumer.seek_to_end())

    def setPort(self, port):
        self.port = port

    def setIP(self, ID):
        self.ID = ID

    def setTopic(self, topic):
        self.topic = topic

    def getPort(self,):
        return(self.port)

    def getIP(self):
        return (self.ID)

    def getTopic(self):
        return (self.topic)

    def getGroup(self):
        return (self.group)

    def startConnection(self):
        idPlusPort = self.ID+":" + str(self.port)
        self.consumer =KafkaConsumer(self.topic,
                         group_id=self.group,
                         bootstrap_servers=[idPlusPort]) # Consume the lastest data

    def getMessage(self, points):
        for messages in self.consumer:
            dic = json.loads(messages.value.decode('ascii'))
            currentPoint = Point(dic['x'], dic['y'])
            print("CONSUMER: getting message.....")
            points.enqueue(currentPoint)
            if(points.size() > 10):
                time.sleep(5)




