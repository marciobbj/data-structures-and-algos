"""
Queues são consideradas estruturas lineares FIFO (First In First Out). E.g. [1, 2, 3].remove() -> [2, 3]
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinearDataStructure:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None


class Queue(LinearDataStructure):
    def peek(self):
        return self.head.data

    def add(self, data):
        node = Node(data)
        if self.tail is not None:
            self.tail.next = node
        if self.head is None:
            self.head = node
        self.tail = node

    def remove(self):
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data

    def empty(self):
        return self.head == None

    def __repr__(self):
        items = ", ".join([str(i) for i in self])
        if not items:
            return "[]"
        return f"[{items}]"

    def __iter__(self):
        head = self.head
        while head:
            yield head.data
            head = head.next


queue = Queue()

queue.add(1)
queue.add(2)
queue.add(3)