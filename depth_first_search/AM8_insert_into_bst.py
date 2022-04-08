class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insert_bst(bst, val) :
    if not bst:
        return Node(val)
    
    def dfs(node, val):

        if node.val == val:
            return

        if node.val > val:
            if node.left:
                dfs(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                dfs(node.right, val)
            else:
                node.right = Node(val)

    dfs(bst, val)

    return bst

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