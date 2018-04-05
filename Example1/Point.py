import time

class Point:
    def __init__ (self, x,y):
        self.x = x
        self.y =  y
        self.kafkaTime = int(round(time.time() * 1000))

    def setX(self, x):
        self.x = x

    def getKafkaTime(self, x):
        return(self.kafkaTime)

    def setY(self, y):
        self.y = y

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)