
def get_answers_hashmap(a,b):
    if len(a[0]) != len(b):
        return None

    n_rows = len(a)
    n_cols = len(b[0])

    output = []

    for i in range(n_rows):
        output.append([0]*n_cols)

    a_map = {}
    b_map = {}

    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                if i not in a_map:
                    a_map[i] = {}
                a_map[i][j] = a[i][j]

    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] != 0:
                if i not in b_map:
                    b_map[i] = {}
                b_map[i][j] = b[i][j]


    for i in range(len(a)):
        if i in a_map:
            for j in range(len(a[0])):
                if j in a_map[i] and j in b_map:
                    for k in range(len(b[j])):
                        if k in b_map[j]:
                            output[i][k] = a_map[i][j] * b_map[j][k]

    return output




def get_answer(a,b):
    if len(a[0]) != len(b):
        return None

    n_rows = len(a)
    n_cols = len(b[0])

    result_matrix = []
    for i in range(n_rows):
        result_matrix.append([0] * n_cols)


    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j] != 0:
                for k in range(len(b[j])):
                    result_matrix[i][k] += a[i][j] * b[j][k]

    return result_matrix


a = [[1, 0, 3], [0, 1, 2]]
b = [[0, 1], [1, 3], [0, 0]]

print(get_answers_hashmap(a,b))