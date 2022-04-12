class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten_tree1(tree):

    def dfs(node):
        if not node:
            return None

        left_tail = dfs(node.left)
        right_tail = dfs(node.right)

        if node.left:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail or left_tail or node

    dfs(tree)

    return tree

def flatten_tree(tree):
    if not tree:
        return None

    head = None
    tail = None
    cur = tree
    stack = []

    while stack or cur:

        while cur:
            stack.append(cur)

            if not head:
                head = Node(cur.val)
                tail = head
            else:
                tail = Node(cur.val)

            tail = tail.right


            cur = cur.left


        cur = stack.pop().right

    return head







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