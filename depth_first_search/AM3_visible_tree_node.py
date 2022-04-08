class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:


    def dfs(node, max_val):
        if not node:
            return 0

        count = 0
        if node.val >= max_val:
            count += 1
            max_val = node.val

        count += dfs(node.left, max_val)
        count += dfs(node.right, max_val)

        return count

    return dfs(root, float('-inf'))


def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)