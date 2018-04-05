class Queue:
    def __init__(self):
        self.items = []
        self.consumerTime = 0
        self.producerTime = 0
        self.graphTime = 0
        self.numberOfItemsSent = 0
        self.numberOfItemsConsume = 0

    def isEmpty(self):
        return len(self.items) < 3

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)