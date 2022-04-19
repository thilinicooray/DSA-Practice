class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    if not root:
        return -1

    from collections import deque

    q  = deque([(root,0)])

    while q:
        ele, lvl = q.popleft()

        is_leaf = True

        if ele.left:
            q.append((ele.left, lvl+1))
            is_leaf = False

        if ele.right:
            q.append((ele.right, lvl +1))
            is_leaf = False

        if is_leaf:
            return lvl




def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter('1 2 4 x 7 x x 5 x x 3 x 6 x x'.split()), int)
    res = binary_tree_min_depth(root)
    print(res)