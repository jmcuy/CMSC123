class Queue:

    def __init__(self):
        self.items = []


    def enqueue(self, item):
        self.items += [item]

    def dequeue(self):
        if self.size() != 0:
            var = self.items[0]
            self.items = self.items[1:]
            return var
        else:
            return None


    def front(self):
        if self.size() != 0:
            return self.items[0]
        else:
            return None

    def rear(self):
        if self.size() != 0:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
