"""
Time Complexity: O(log N)
"""


def binary_search(array, x, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
    if array[mid] == x:
        return array.index(x)
    elif x < array[mid]:
        return binary_search(array, x, left, mid - 1)
    return binary_search(array, x, mid + 1, right)


a = [c for c in range(1000000)]

b = binary_search(a, 3990, 0, 1000000)
print(b)