from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:

    idx = -1
    l = 0
    r = len(arr) -1

    while l <= r:
        mid = (l+r)//2

        if arr[mid] >= target:
            idx = mid
            r = mid -1

        else:
            l = mid +1


    return idx


'''print(first_not_smaller([i for i in range(7)], 3))
print(first_not_smaller([i for i in range(7)], 2))
print(first_not_smaller([i for i in range(7)], 5))'''

print(first_not_smaller([0], 0))