class Graph:
    def __init__(self, plt):
        self.plt = plt

    def setAxis(self, x0,x1,y0,y1):
        self.plt.axis([x0, x1, y0, y1])

    def addPoint(self,point):
        self.lastPont = point
        self.plt.scatter(point.getX(), point.getY())

##################################################################
##################  Adding Random Point   ########################
##################################################################

    # def addRandomPoint(self):
    #     y = np.random.random()
    #     ranPoint = Point(self.lastPont.getX() + 1,y)
    #     self.addPoint(ranPoint)