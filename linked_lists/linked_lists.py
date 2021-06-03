class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_last(self, node):
        if self.head is None:
            # if is the first item then just set the head
            self.head = node
            return
        for current_node in self:
            # transverse the hole list
            pass
        # set the last item `next` to the new node
        current_node.next = node

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("list is empty")

        for node in self:
            if node.val == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("data is not found")

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("list empty")

        if self.head.val == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.val == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node
        raise Exception("data is not found")

    def remove(self, target_node_data):
        if self.head is None:
            raise Exception("empty list")
        prev_node = self.head
        for node in self:
            if node.val == target_node_data:
                node.next = None
                node.val = None
                prev_node.next = node.next
                return
            prev_node = node
        raise Exception("data not found")

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


n4 = Node("fourth")
n3 = Node("third", n4)
n2 = Node("second", n3)
head = Node("first", n2)

# first -> second -> third -> fourth
l1 = LinkedList(head)


def nth_from_end(head, nth):
    """Gets the nth element from a Linked List counting from the end.

    e.g.

    head = 1 -> 2 -> 3 -> 4 -> None

    nth_from_end(head, 2)
    -> 3
    nth_from_end(head, 5)
    -> None
    nth_from_end(head, None)
    -> None
    """
    curr_node = head
    linked_list_length = 0

    if not nth:
        return None

    while True:
        _next_node = curr_node.next
        if _next_node is None:
            break
        curr_node = _next_node
        linked_list_length += 1

    if nth > linked_list_length + 1:
        return None

    reverse_index = (linked_list_length + 1) - nth

    if reverse_index == 0:
        return head.val

    node = head

    for _ in range(reverse_index):
        _next_node = node.next
        node = _next_node

    return node.val


print("add first element")
l1.add_first(Node("new_head"))
print(l1)

print("add first element")
l1.add_last(Node("new last node hehe"))
print(l1)

print("add element after first")
l1.add_after("first", Node("node after first"))
print(l1)

print("add element before third")
l1.add_before("third", Node("node before third"))
print(l1)

print("remove second element")
l1.remove("second")
print(l1)

print(nth_from_end(head, 1))
print(nth_from_end(head, 2))
print(nth_from_end(head, 3))
print(nth_from_end(head, 4))