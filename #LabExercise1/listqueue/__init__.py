from linkedlist import LinkedList


class Queue:

    def __init__(self):
        self.items = LinkedList()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        current = self.items.head
        if current is None:
            return None
        else:
            return self.items.remove(current.value).value


    def front(self):
        current = self.items.head
        if current:
            return self.items.head.value
        else:
            return None
        pass

    def rear(self):
        current = self.items.head
        if current is not None:
            while current.next is not None:
                current = current.next
            return current.value
        else:
            return None



    def size(self):
        return self.items.size()



