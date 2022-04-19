
def metrix_as_graph(matrix):
    num_rows = len(matrix)
    num_col = len(matrix[0])

    def get_neighbours(x,y):
        delta_row = [0,-1,0,1]
        delta_col = [-1,0,1,1]

        neighbours = set()

        for i in range(len(delta_row)):
            n_r = x+delta_row[i]
            n_c = y+delta_col[i]

            if 0 <= n_r < num_rows and 0<= n_c < num_col:
                neighbours.add((n_r,n_c))

        return neighbours

    def bfs(graph):

        if not graph:
            return None

        from collections import deque

        q = deque([(0,0)])
        visited = set()

        while q:
            x,y = q.popleft()

            visited.add((x,y))
            
            neighbours = get_neighbours(x,y)

            for n in neighbours:
                #todo
                q.append(n)