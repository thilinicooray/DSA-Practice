class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(root):
    all  = []
    def dfs(node):
        if not node:
            all.append('x' )
            return

        all.append(node.val)

        dfs(node.left)
        dfs(node.right)

    dfs(root)

    return ' '.join(all)


def deserialize(s):

    from collections import deque



    q = deque(list(s))

    def dfs():

        if not q:
            return

        char = q.popleft()

        if char == 'x':
            return

        node = Node(char)
        node.left = dfs()
        node.right = dfs()

        return node

    return dfs()


input = '643xx5xx8xx'

root = deserialize(input)
print('made tree :')
#print_tree(root)

print(serialize(root))



