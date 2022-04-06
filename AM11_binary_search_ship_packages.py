
from typing import List

def check_feasibility(weights, capacity, days):

    req_days = 1
    cur_cap = capacity

    for w in weights:
        if w > capacity:
            return False
        else:
            cur_cap = cur_cap - w

            if cur_cap < 0:
                cur_cap = capacity - w
                req_days += 1


    return req_days <= days


def min_max_weight(weights: List[int], d: int) -> int:

    l = max(weights)
    r = sum(weights)

    min_cap = -1

    while l <= r:
        mid = (l+r)//2

        is_feasible = check_feasibility(weights, mid, d)

        if is_feasible:
            min_cap = mid
            r = mid -1
        else:
            l = mid +1

    return min_cap
