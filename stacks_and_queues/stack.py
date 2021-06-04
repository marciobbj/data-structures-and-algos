"""
Stacks sao consideradas estruturas lineares LIFO (Last In First Out). E.g. [1, 2, 3].pop() -> [1, 2]
"""


from stacks_and_queues import LinearDataStructure, Node


class Stack(LinearDataStructure):
    def empty(self):
        return self.head == None

    def peek(self):
        return self.head.data

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        return data

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


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
