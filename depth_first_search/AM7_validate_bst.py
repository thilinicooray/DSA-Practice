
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root):

    def dfs(node, min, max):
        if not node:
            return True

        if not (min <= node.val <= max):
            return False

        return dfs(node.left, min, node.val) and dfs(node.right, node.val, max)

    return dfs(root, float('-inf'), float('inf'))



def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    input = '9 6 3 2 x x 4 x x 5 x x 11 10 x x 19 x x'
    root = build_tree(iter(input.split()), int)
    res = valid_bst(root)
    print('true' if res else 'false')