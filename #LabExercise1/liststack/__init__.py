from linkedlist import LinkedList


class Stack:

    def __init__(self):
        self.items = LinkedList()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        current = self.items.head
        if current is not None:
            return self.items.remove(self.peek()).value
        else:
            return None

    def peek(self):
        current = self.items.head
        if current:
            while current.next is not None:
                current = current.next
            return current.value
        else:
            return None

    def size(self):
        return self.items.size()
