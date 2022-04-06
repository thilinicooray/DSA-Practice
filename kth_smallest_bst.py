
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None
        self.visited = False

class Tree:

    def kth_smallest(self, root, k):
        #dfs iter
        stack = []
        #root.visited = True
        count = 0
        #value = 0
        cur = root
        while stack and cur:


            while cur:
                stack.append(cur)
                #leftc.visited = True
                cur = cur.left

            cur = stack.pop()

            count +=1

            if count == k:
                return cur.value

            cur = cur.right






