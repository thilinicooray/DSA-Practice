
from collections import deque
import copy

def get_min_steps(board):
    m, n = len(board), len(board[0])
    grid = [''.join([str(x) for x in l]) for l in board]
    grid = ''.join(grid)

    q = deque([grid])
    visited = set(grid)
    step = 0
    while(q):
        for _ in range(len(q)):
            mat = q.popleft()
            if mat == '123450':
                return step
            a = mat.index('0')
            x, y = a//n, a%n

            # transfer 1d-index of zero to 2d-index to get the neighbor

            for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0<=nx<m and 0<=ny<n:
                    # transfer 1d-index of neighbor to 2d-index for further switching
                    b = nx*n+ny
                    nxt = list(mat)
                    nxt[a], nxt[b] = nxt[b], nxt[a]
                    nxt = ''.join(nxt)
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append(nxt)
        step += 1

    return -1


puzzle = [[4, 1, 3], [2, 0, 5]]

print('min steps to solve the puzzle is {}'.format(get_min_steps(puzzle)))