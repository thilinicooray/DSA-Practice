from typing import List

def check_feasibility(papers, worker_count, max_time):
    cur_workers = 1
    req_time = max_time

    for paper in papers:
        if paper > max_time:
            return False
        else:
            req_time = req_time - paper

            if req_time < 0:
                cur_workers +=1
                req_time = max_time - paper

    return cur_workers <= worker_count



def newspapers_split(newspapers: List[int], coworkers: int) -> int:
    l = max(newspapers)
    r = sum(newspapers)

    min_time = -1

    while l <= r:
        mid = (l+r) //2

        is_feasible = check_feasibility(newspapers, coworkers, mid)

        if is_feasible:
            min_time = mid
            r = mid -1
        else:
            l = mid +1

    return min_time