from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    if not arr :
        return -1

    idx = -1
    l = 0
    r = len(arr) -1

    while l <= r:
        mid = (l+r) //2

        if arr[mid] ==target:
            idx = mid
            r = mid -1

        elif arr[mid] > target:
            r = mid -1
        else:
            l = mid +1

    return idx