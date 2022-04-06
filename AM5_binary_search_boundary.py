from typing import List

def find_boundary(arr: List[bool]) -> int:
    if not arr:
        return -1

    if not any(arr):
        return -1

    l = 0
    r = len(arr) -1

    idx = -1

    while l <= r :
        mid = (l + r) //2

        if arr[mid]:
            idx = mid
            r = mid -1
        else:
            l = mid +1

    return idx


arr1 = [False, False, True, True, True, True, True]
print(find_boundary(arr1))

arr1 = [False, False, False, False, True, True, True]
print(find_boundary(arr1))

arr1 = [False, False, False, False, False, True, True]
print(find_boundary(arr1))

arr1 = [False, False, False, False, False, False, False]
print(find_boundary(arr1))