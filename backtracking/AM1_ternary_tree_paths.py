from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root):
    if not root:
        return []

    def dfs(node,path, res):
        path.append(str(node.val))

        if all(c is None for c in node.children):
            res.append('->'.join(path))
            return

        for child in node.children:
            if child:
                dfs(child, path, res)
                path.pop()

    res = []
    dfs(root,[], res)

    return res

def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)