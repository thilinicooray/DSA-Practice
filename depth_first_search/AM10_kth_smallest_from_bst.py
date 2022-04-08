class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(bst, k):
    if not bst:
        return -1

    count = 0
    stack = []
    cur = bst
    while stack or cur:

        while cur:
            stack.append(cur)
            cur = cur.left

        out = stack.pop()
        count +=1

        if count == k:
            return out.val

        cur = out.right



    return -1




def build_tree(nodes, f):
    val = next(nodes)
    if val == 'x': return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == '__main__':
    input = '37 19 2 x x 28 23 x x 35 x x 44 x 58 52 x x 67 x x'
    bst = build_tree(iter(input.split()), int)
    k = int(8)
    res = kth_smallest(bst, k)
    print(res)