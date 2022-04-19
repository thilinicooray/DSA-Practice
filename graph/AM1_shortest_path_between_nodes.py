from typing import List

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    if not graph:
        return -1

    if a== b:
        return 0

    visited = set()
    len = 1

    from collections import deque

    q = deque([a])

    while q:
        val = q.popleft()
        visited.add(val)

        neighbours = graph[val]

        for neighbour in neighbours:
            if neighbour not in visited:
                if neighbour == b:
                    return len
                q.append(neighbour)

        len += 1

    return -1


if __name__ == '__main__':
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    a = int(input())
    b = int(input())
    res = shortest_path(graph, a, b)
    print(res)