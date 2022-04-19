from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zig_zag_traversal(root: Node) -> List[List[int]]:
    if not root:
        return []

    from collections import deque

    q = deque([(root ,1)])
    levels = []
    is_reverse = True
    while q:
        ele, lev = q.popleft()
        if len(levels) < lev:
            levels.append(deque([ele.val]))
            is_reverse = not is_reverse
        else:
            if is_reverse:
                levels[lev -1].appendleft(ele.val)
            else:
                levels[lev -1].append(ele.val)


        if ele.left:
            q.append((ele.left, lev+1))

        if ele.right:
            q.append((ele.right, lev+1))

    return levels

def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    root = build_tree(iter('1 2 4 x 7 x x 5 x 8 x x 3 x 6 x x'.split()), int)
    res = zig_zag_traversal(root)
    for row in res:
        print(' '.join(map(str, row)))