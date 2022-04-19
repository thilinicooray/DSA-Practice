from typing import List

def count_number_of_islands(grid: List[List[int]]) -> int:
    if not grid:
        return -1

    n_rows = len(grid)
    n_col = len(grid[0])
    visited = set()

    def get_neighbours(x,y):
        delta_r = [0,-1,0,1]
        delta_c = [-1,0,1,0]

        neighbours = set()

        for i in range(len(delta_r)):
            n_x = x + delta_r[i]
            n_y = y + delta_c[i]

            if 0 <= n_x < n_rows and 0 <= n_y < n_col:
                neighbours.add((n_x, n_y))

        return neighbours

    def bfs(x,y):

        from collections import deque
        q = deque([(x,y)])

        while q:
            x,y = q.popleft()
            visited.add((x,y))

            neighbours = get_neighbours(x,y)

            for n in neighbours:
                if n not in visited and grid[n[0]][n[1]] == 1:
                    q.append(n)

    n_isle = 0
    for r in range(n_rows):
        for c in range(n_col):
            if grid[r][c] == 1 and (r,c) not in visited:
                n_isle += 1
                bfs(r,c)

    return n_isle




if __name__ == '__main__':
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)