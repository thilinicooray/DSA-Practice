class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def cycle_size(nodes: Node) -> int:
    if not nodes:
        return -1

    slow = nodes
    fast = nodes

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break

    if not fast or not fast.next:
        return -1

    count = 0

    while fast and fast.next:
        count += 1
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return count


if __name__ == '__main__':
    raw_input = [int(x) for x in input().split()]
    nodes_list = []
    for i, entry in enumerate(raw_input):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = cycle_size(nodes)
    print(res)
