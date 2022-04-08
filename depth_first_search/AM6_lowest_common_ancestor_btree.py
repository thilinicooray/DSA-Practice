class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root, node1, node2):
    if not root:
        return None

    l1 = dfs(root,  node1.val)
    l2 = dfs(root,  node2.val)

    l_an = None

    while l1 and l2:
        l1_out = l1.pop()
        l2_out = l2.pop()

        if l1_out == l2_out:
            l_an = l1_out
        else:
            break

    return l_an


def dfs(node, target):
    if not node:
        return None

    if node.val == target:
        return [node]

    cur = dfs(node.left, target) or dfs(node.right, target)

    if cur:
        cur.append(node)

    return cur


'''
def lca(root, node1, node2):
    if not root:
        return

    # case 2 in above figure
    if root == node1 or root == node2:
        return root

    left = lca(root.left, node1, node2)
    right = lca(root.right, node1, node2)

    # case 1
    if left and right:
        return root

    # at this point, left and right can't be both non-null since we checked above
    # case 4 and 5, report target node or LCA back to parent
    if left:
        return left
    if right:
        return right

    # case 4, not found return null
    return None'''

if __name__ == "__main__":
    # driver code, do not modify
    tree = '6 4 3 x x 5 x x 8 x x'
    n1 = '4'
    n2 = '8'
    def build_tree(nodes):
        val = next(nodes)
        if not val or val == 'x': return
        cur = Node(val)
        cur.left = build_tree(nodes)
        cur.right = build_tree(nodes)
        return cur
    def find_node(root, target):
        if not root: return
        if root.val == target: return root
        return find_node(root.left, target) or find_node(root.right, target)
    s = tree.split()
    #print('split tree', s)
    root = build_tree(iter(s))
    node1 = find_node(root, n1)
    node2 = find_node(root, n2)
    ans = lca(root, node1, node2)
    if not ans: print('null')
    else: print(ans.val)



