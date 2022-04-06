
def find_missing(arr):
    arr_len = len(arr)

    tot = 0

    for i in range(arr_len):
        tot += (i+1)

    tot_cur = 0

    for j in arr:
        tot_cur += j

    missing = tot - tot_cur

    return missing