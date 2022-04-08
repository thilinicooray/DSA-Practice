class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_tree(tree):
    if not tree:
        return None



    def dfs(node, flatten_tree):
        if not node:return flatten_tree

        if not flatten_tree:
            flatten_tree = Node(node.val)

        else:
            flatten_tree.right = Node(node.val)
            flatten_tree = flatten_tree.right

        flatten_tree = dfs(node.left, flatten_tree)
        flatten_tree = dfs(node.right, flatten_tree)

        return flatten_tree

    return dfs(tree, None)


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
    #yield from format_tree(node.left)
    #yield from format_tree(node.right)



if __name__ == '__main__':
    input = '1 2 4 x x 5 x x 3 x x'
    tree = build_tree(iter(input.split()), int)
    res = flatten_tree(tree)
    #print(' '.join(format_tree(res)))
    while res:
        print(res.val)
        print(res.left)
        res = res.right