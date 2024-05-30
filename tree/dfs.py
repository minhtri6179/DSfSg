def dfs_pre_order(root):
    if root is None:
        return []
    res = []
    stack = [root]
    while stack:
        cur_node = stack.pop()
        res.append(cur_node.value)
        if cur_node.left:
            stack.append(cur_node.left)
        elif cur_node.right:
            stack.append(cur_node.right)

    return res
