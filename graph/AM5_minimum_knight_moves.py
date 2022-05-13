

def get_knight_shortest_path(x: int, y: int) -> int:
    max_rows = x+2
    max_col = y+2

    def get_neighbours(a,b):
        rows = [-2,-1,-2,-1,1,2,2,1]
        cols = [-1,-2,1,2,2,1,-1,-2]

        neighbours = set()

        for i in range(len(rows)):
            r = a + rows[i]
            c = b + cols[i]

            if -2 <= r <= max_rows and -2 <= c <= max_col:
                neighbours.add((r,c))

        return neighbours

    from collections import deque

    q = deque([(0,0,0)])

    visited = set()

    min_moves = float('infinity')

    while q:
        a,b,move = q.popleft()

        visited.add((a,b))

        if (a,b) == (x,y) and move < min_moves:
            min_moves = move

        neighbours = get_neighbours(a,b)

        for n in neighbours:
            if n not in visited:
                q.append((n[0],n[1], move + 1))

    return min_moves


if __name__ == '__main__':
    x = int(3)
    y = int(3)
    res = get_knight_shortest_path(x, y)
    print(res)