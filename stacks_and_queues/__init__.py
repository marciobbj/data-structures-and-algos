class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinearDataStructure:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None