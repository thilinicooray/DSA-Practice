class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:

    def dfs(node):
        if not node:
            return 0

        l_height = dfs(node.left)
        r_height = dfs(node.right)

        if abs(l_height - r_height) > 1:
            return -1

        if l_height == -1 or r_height== -1:
            return -1

        return max(l_height, r_height) +1

    return dfs(tree) != -1










def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)