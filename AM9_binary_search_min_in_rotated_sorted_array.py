from typing import List

def find_min_rotated(arr: List[int]) -> int:
    '''if not arr:
        return -1

    l = 0
    r = len(arr) -1

    while l <= r:
        left = arr[l]
        right = arr[r]
        if left <= right:
            return l
        else:
            l = l+1'''

    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index


arr = [10,20,30,40,50,60,70]

print(find_min_rotated(arr))

arr = [20,30,40,50,60,70,10]

print(find_min_rotated(arr))

arr = [30,40,50,60,70,10,20]

print(find_min_rotated(arr))

arr = [50,60,70,10,20,30,40]

print(find_min_rotated(arr))

arr = [50,60,10,10,10,20,30,40]

print(find_min_rotated(arr))

arr = [50]

print(find_min_rotated(arr))

