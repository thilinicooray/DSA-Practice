"""
given a binary tree, get the average value at each level of the tree
Input

        4
       / \
      7   9
     / \   \
    10 2   6
       \
        6
       /
      2
output : [4,8,6,6,2]
"""

from collections import deque

class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None


def level_avg_binary_tree(root):

    if not root:
        return []


    level_avg = {}
    tree_q = deque([(root,1)])
    avg = []

    while tree_q:
        node,lvl = tree_q.popleft()

        if lvl not in level_avg:
            level_avg[lvl] = (node.value)

        else:
            value = level_avg[lvl]
            new_val = value + node.value
            level_avg[lvl] = new_val /2

        if node.left:
            tree_q.append(node.left,lvl+1)
        if node.right:
            tree_q.append(node.right,lvl+1)


    level_count = len(level_avg.keys())

    for i in range(level_count):
        avg.append(level_avg[i+1])

    return avg



