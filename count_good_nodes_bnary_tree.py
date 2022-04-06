from collections import deque

class Node:
    def __init__(self, v):
        self.value = v
        self.left = None
        self.right = None


def find_good_nodes(root):
    if not root:
        return []

    q = deque([(root, True, root.value)])

    good_nodes = 0

    while q:
        node, is_good, max_val = q.popleft()

        if is_good:
            good_nodes += 1

        if node.left:
            q.append((node.left, (node.left.value >= max_val), max(max_val,node.left.value) ))

        if node.right:
            q.append((node.right, (node.right.value >= max_val), max(max_val, node.right.value)))


    return good_nodes

def good_nodes_tree(root):

    def find_good_nodes_dfs(root, max):
        if not root:
            return 0
        count = 0
        if root.value >= max:
            count = 1

        max_val = max(max,root.value)

        return count + find_good_nodes_dfs(root.left, max_val) + find_good_nodes_dfs(root.right, max_val)

    return find_good_nodes_dfs(root, root.value)

