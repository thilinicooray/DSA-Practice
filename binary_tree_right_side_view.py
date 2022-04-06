from collections import deque
class Node:
    def __init__(self,v):
        self.value = v
        self.left = None
        self.right = None


class Tree:
    def right_view(self, root):
        visible_nodes = []
        q = deque([(root,1)])

        while q :
            node, lvl = q.popleft()

            if len(visible_nodes) >= lvl:
                visible_nodes[lvl-1] = node.value
            else:
                visible_nodes.append(node.value)



            if node.left:
                q.append((node.left, lvl+1))

            if node.left:
                q.append((node.left, lvl+1))

        return visible_nodes

    
