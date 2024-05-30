from collections import deque


def bfs_queue(root):
    if root is None:
        return
    q = deque([root])
    res = []
    while q:
        tmp = []
        for _ in range(len(q)):
            cur_node = q.popleft()
            if cur_node:
                tmp.append(cur_node.value)
                q.append(cur_node.left)
                q.append(cur_node.right)
        if tmp:
            res.append(tmp)
    return res
