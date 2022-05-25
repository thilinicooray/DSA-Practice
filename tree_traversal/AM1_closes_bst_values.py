

from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def closest_values(bst: Node, x: int, k: int) -> List[int]:
    stack = []
    from collections import deque
    q = deque()
    cur = bst
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left

        cur = stack.pop()

        if len(q) < k:
            q.append(cur.val)
        else:
            if abs(q[0]-x) > abs(cur.val -x):
                q.popleft()
                q.append(cur.val)
            else:
                break

        cur = cur.right

    return list(q)







def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    bst = build_tree(iter(input().split()), int)
    x = int(input())
    k = int(input())
    res = closest_values(bst, x, k)
    print(' '.join(map(str, res)))