from kafka import KafkaClient
from kafka import KafkaConsumer
from Consumer.Point import Point
import json

class Consumer:
    def __init__(self):
        self.port = 9092
        self.ID = 'localhost'
        self.topic = 'test'
        self.group = 'mygroup'


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
                         group_id=None,
                         bootstrap_servers=[idPlusPort],
                         auto_offset_reset='smallest')

    def getMessage(self, points):
        # self.consumer.seek_to_beginning()
        for messages in self.consumer:
            dic = json.loads(messages.value.decode('ascii'))
            currentPoint = Point(dic['x'], dic['y'])
            print("CONSUMER: getting message.....")
            points.enqueue(currentPoint)
            # if(points.size() > 10):
            #     time.sleep(5)




