# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque([(root,1)])

        level_order = []

        while q:
            node, lvl = q.popleft()

            if len(level_order) < lvl:
                level_order.append([node.val])
            else:
                level_order[lvl-1].append(node.val)

            lvl += 1

            if node.left:
                q.append((node.left,lvl))
            if node.right:
                q.append((node.right, lvl))

        return level_order

