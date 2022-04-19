from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
    if not root:
        return []

    from collections import deque

    q = deque([(root, 1)])

    right_most = []

    while q:
        ele, lev = q.popleft()

        if len(right_most) < lev:
            right_most.append(ele.val)
        else:
            right_most[lev-1] = ele.val

        if ele.left:
            q.append((ele.left, lev+1))

        if ele.right:
            q.append((ele.right, lev+1))

    return right_most

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter('1 2 4 x 7 x x 5 x x 3 x 6 x x'.split()), int)
    res = binary_tree_right_side_view(root)
    print(' '.join(map(str, res)))