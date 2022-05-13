from typing import List
from collections import deque

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    if not dungeon_map:
        return []

    max_rows = len(dungeon_map)
    max_cols = len(dungeon_map[0])

    def get_neighbours(x,y):
        delta_row = [0,-1,0,1]
        delta_col = [-1,0,1,0]
        neighbours = set()

        for i in range(len(delta_row)):
            x_new = x + delta_row[i]
            y_new = y + delta_col[i]

            if 0 <= x_new < max_rows and 0 <= y_new < max_cols and dungeon_map[x_new][y_new] != -1:
                neighbours.add((x_new, y_new))

        return neighbours


    def get_step_count_to_exit(r,c):
        min_steps = dungeon_map[r][c]
        q = deque([(r, c, 0)])
        visited = set()

        while q:
            x,y,step = q.popleft()
            visited.add((x,y))
            if dungeon_map[x][y] == 0 and step < min_steps:
                min_steps = step

            neighbours = get_neighbours(x,y)

            for n in neighbours:
                if n not in visited:
                    q.append((n[0], n[1], step+1))

        return min_steps

    for r in range(max_rows):
        for c in range(max_cols):
            if dungeon_map[r][c] != 0 and dungeon_map[r][c] != -1:
                dungeon_map[r][c] = get_step_count_to_exit(r,c)

    return dungeon_map

def map_gate_distances_fast(dungeon_map: List[List[int]]) -> List[List[int]]:
    if not dungeon_map:
        return []

    INF = 2147483647

    max_rows = len(dungeon_map)
    max_cols = len(dungeon_map[0])

    q = deque()

    for r in range(max_rows):
        for c in range(max_cols):
            if dungeon_map[r][c] == 0 :
                q.append((r,c))

    def get_neighbours(x,y):
        delta_row = [0,-1,0,1]
        delta_col = [-1,0,1,0]
        neighbours = set()

        for i in range(len(delta_row)):
            x_new = x + delta_row[i]
            y_new = y + delta_col[i]

            if 0 <= x_new < max_rows and 0 <= y_new < max_cols and dungeon_map[x_new][y_new] == INF:
                neighbours.add((x_new, y_new))

        return neighbours


    while q:
        x,y = q.popleft()

        neighbours = get_neighbours(x,y)

        for n in neighbours:
            dungeon_map[n[0]][n[1]] = dungeon_map[x][y] + 1
            q.append((n[0], n[1]))



    return dungeon_map

if __name__ == '__main__':
    #dungeon_map = [[int(x) for x in input().split()] for _ in range(int(input()))]
    dungeon_map =[
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
    res = map_gate_distances_fast(dungeon_map)
    for row in res:
        print(' '.join(map(str, row)))