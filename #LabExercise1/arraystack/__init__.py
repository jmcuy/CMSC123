class Stack:

    def __init__(self):
        self.items = []


    def push(self, item):
        self.items += [item]


    def pop(self):
        if self.size() != 0:
            last = self.items[-1]
            self.items = self.items[:-1]
            return last
        else:
            return None

    def peek(self):
        if self.size() != 0:
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)
