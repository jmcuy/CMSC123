from node import LinkedListNode

class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        nodes = LinkedListNode(item,None)
        nodes.next = self.head
        self.head = nodes
        return nodes

    def append(self, item):
        nodes = LinkedListNode(item, None)
        current = self.head
        if current:
            while current.next is not None:
                current = current.next
            current.next = nodes
        else:
            self.head = nodes
        return nodes

    def insert(self, item, position):
        nodes = LinkedListNode(item, None)
        current = self.head
        if position == 0:
            nodes.next = current
            self.head = nodes
        else:
            count = 0
            while count < position - 1 and current.next is not None:
                current = current.next
                count += 1
            nodes.next = current.next
            current.next = nodes
        return nodes

    def remove(self, item):
       current = self.head
       if current is None:
           return None
       if current.value == item:
           self.head = current.next
           current.next = None
           return current
       else:
           nodes = None
           while current.next is not None and current.next.value != item:
               current = current.next
           if current.next is None:
             return None
           nodes = current.next
           current.next = current.next.next
           nodes.next = None
           return nodes


    def search(self, item):
        items = LinkedListNode(item,None)
        current = self.head
        while current:
            if current.value == items.value:
                return True
            else:
                current = current.next
        return False

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

