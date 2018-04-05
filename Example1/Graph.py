import numpy as np
from Example1.Point import Point
class Graph:
    def __init__(self, plt):
        self.plt = plt

    def setAxis(self, x0,x1,y0,y1):
        self.plt.axis([x0, x1, y0, y1])

    def addPoint(self,point):
        self.lastPont = point
        self.plt.scatter(point.getX(), point.getY())

    def addRandomPoint(self):
        y = np.random.random()
        ranPoint = Point(self.lastPont.getX() + 1,y)
        self.addPoint(ranPoint)




# plt.axis([0, 1000, 0, 1])
# plt.ion()
#
# for i in range(1000):
#     y = np.random.random()
#     plt.scatter(i, y)
#     plt.pause(0.05)
#
# while True:
#     plt.pause(0.05)