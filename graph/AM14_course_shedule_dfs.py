
def replace_q(q,b):
    if len(q) != 3:
        #Invalid query
        return

    i = q[1]
    x = q[2]
    b[i] = x

def sum_pairs(q,a,b):

    if len(q) != 2:
        #Invalid query
        return -1

    b_dict = {}
    sum = q[-1]

    # create a map for array a for constant lookup as its size could larger than array b
    for item in a:

        if item not in b_dict:
            b_dict[item] = 0
        b_dict[item] += 1

    pairs = 0

    for ele in b:
        remain = sum - ele

        # finding the indices in array a which has the value "remain"
        if remain in b_dict:
            re_idx = b_dict[remain]

            pairs += re_idx


    return pairs

def solution(a, b, queries):

    #a_dict = {}
    #b_dict = {}

    res = []

    for q in queries:
        if len == 0:
            # invalid query
            continue

        q_type = q[0]

        if q_type == 0:
            replace_q(q,b)
        elif q_type == 1:
            sum_q = sum_pairs(q,a,b)
            if sum_q != -1:
                res.append(sum_q)
        else:
            print('Invalid query type!')

    return res



