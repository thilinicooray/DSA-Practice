class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_binary_tree(tree):
    if not tree:
        return None

    def dfs(node):
        if not node:
            return None

        dfs(node.left)
        dfs(node.right)

        val  = node.left
        node.left = node.right
        node.right = val

    dfs(tree)

    return tree

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

def format_tree(node):
    if node is None:
        yield 'x'
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)