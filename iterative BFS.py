from collections import deque

class Node:
    left = right = None
    def __init__(self, value):
        self.value = value


root = Node(4)
root.left = Node(2)
root.right = Node(6)

root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)


def DFS(root):
    queue = deque()
    queue.appendleft(root)

    while queue:
        node = queue.pop()
        print(node.value)

        if node.left:
            queue.appendleft(node.left)

        if node.right:
            queue.appendleft(node.right)


DFS(root)