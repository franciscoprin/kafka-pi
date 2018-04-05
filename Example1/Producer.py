from kafka import KafkaClient
from kafka import SimpleProducer
import json

class Producer:
    def __init__(self):
        self.port = 9092
        self.IP = 'localhost'
        self.topic = 'test'

    def setPort(self, port):
        self.port = port

    def setIP(self, ID):
        self.IP = ID

    def setTopic(self, topic):
        self.topic = topic

    def getPort(self,):
        return(self.port)

    def getID(self):
        return (self.IP)

    def getTopic(self):
        return (self.topic)

    def startConnection(self):
        idPlusPort = self.IP + ":" + str(self.port)
        kafka = KafkaClient(idPlusPort)
        self.producer = SimpleProducer(kafka, async=True)

    def sendMessage(self, msg):
        msg_json = json.dumps(msg, default=lambda o: o.__dict__)
        msg_json_string = str(msg_json)
        msg_json_string_bytes = str.encode(msg_json_string)
        self.producer.send_messages(self.getTopic(), msg_json_string_bytes)

