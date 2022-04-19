from typing import List

def flood_fill(r: int, c: int, replacement: int, image: List[List[int]]) -> List[List[int]]:

    if not image:
        return image

    n_rows = len(image)
    n_col = len(image[0])

    if 0 > r or r >= n_rows or 0 > c or c >= n_col:
        return image

    def get_neighbours(x,y):


        delta_r = [0,-1,0,1]
        delta_c = [-1,0,1,0]

        neighbours = set()

        for i in range(len(delta_r)):
            n_x = x + delta_r[i]
            n_y = y + delta_c[i]

            if 0 <= n_x < n_rows and 0 <= n_y < n_col:
                neighbours.add((n_x,n_y))

        return neighbours

    from collections import deque

    q = deque([(r,c)])
    org_col = image[r][c]
    while q:
        r,c = q.popleft()
        image[r][c] = replacement

        neighbours = get_neighbours(r,c)

        for n in neighbours:
            n_r, n_c = n
            if image[n_r][n_c] == org_col:
                q.append(n)

    return image

if __name__ == '__main__':
    r = int(input())
    c = int(input())
    replacement = int(input())
    image = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(' '.join(map(str, row)))