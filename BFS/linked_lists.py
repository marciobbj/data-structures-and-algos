class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head


n4 = Node("fourth", None)
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


print(nth_from_end(head, 1))
print(nth_from_end(head, 2))
print(nth_from_end(head, 3))
print(nth_from_end(head, 4))