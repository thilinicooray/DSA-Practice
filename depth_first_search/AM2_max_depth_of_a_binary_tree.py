class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def tree_max_depth(root:Node)-> int:

    def dfs(node, level):
        if not node:
            return 0

        current_level = level + 1

        return max(current_level, dfs(node.left, current_level),dfs(node.right, current_level))

    return dfs(root,0)

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)