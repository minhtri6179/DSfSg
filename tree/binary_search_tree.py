from collections import deque
from bfs import bfs_queue
from dfs import dfs_pre_order


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(root, value):
    if root is None or root.value == value:
        return root
    if root.value < value:
        return search(root.right, value)
    return search(root.left, value)


def insert(root, value):
    if root is None:
        return Node(value)
    if root.value < value:
        root.right = insert(root.right, value)
    else:
        root.left = insert(root.left, value)
    return root


def find_min(root):
    if root is None:
        return None
    cur = root
    while cur and cur.left:
        cur = cur.left

    return cur


def remove(root, value):
    if not root:
        return None
    if root.value < value:
        root.right = remove(root.right, value)
    elif root.value > value:
        root.left = remove(root.left, value)
    else:
        if not root.left:
            return root.left
        elif not root.right:
            return root.right
        else:
            min_node = find_min(root.right)
            root.value = min_node.value
            root.right = remove(root.right, min_node.value)

    return root


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print(root.value, end=" ")
    in_order(root.right)


def pre_order(root):
    if root is None:
        return
    print(root.value, end=" ")
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.value, end=" ")


def bfs(root):
    if not root:
        return
    queue = deque([root])
    while queue:
        for _ in range(len(queue)):
            cur_node = queue.popleft()
            if cur_node:
                print(cur_node.value, end=" ")
                queue.append(cur_node.left)
                queue.append(cur_node.right)

        print()


root = Node(20)
insert(root, 10)
insert(root, 30)
insert(root, 8)
insert(root, 12)
insert(root, 25)
insert(root, 40)

print("\nIn order ")
in_order(root)
print("\nPost order ")
post_order(root)
print("\nPre order ")
pre_order(root)

print("\nsearching....")

search(root, 26)

print("\n BFS traversal")
bfs(root)

print("\nTree after remove node 20")
remove(root, 20)
in_order(root)

print("\n BFS traversal after remove node 20")
bfs(root)


print("BFS without using recursion")
print(bfs_queue(root))

print("\n #########DFS without recursion##########")
print("Pre-order")
print(dfs_pre_order(root))
print("In-order")
print("Post-order")
