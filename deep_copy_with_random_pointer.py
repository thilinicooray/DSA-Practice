"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        copy = {None:None}
        cur = head
        while cur:
            deepcopy = Node(cur.val)
            copy[cur] = deepcopy
            cur = cur.next

        cur = head

        while cur:
            node = copy[cur]
            node.next = copy[cur.next]
            node.random = copy[cur.random]
            cur = cur.next

        return copy[head]
