# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        stack = [root]
        cur = root
        while cur and stack:
            while cur.left:
                if cur.left.val > cur.val:
                    return False

                stack.append(cur.left)
                cur = cur.left

            cur = stack.pop()

            if cur.right:
                if cur.val > cur.right.val:
                    return False
                stack.append(cur.right)
                cur = cur.right

        return True


