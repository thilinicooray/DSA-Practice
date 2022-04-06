from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    if not arr or len(arr) < 3:
        return -1

    l = 0
    r = len(arr) -1
    idx = -1
    arr.append(-10000000)

    while l <= r:
        mid  = (l+r) //2
        if arr[mid] < arr[mid+1]:
            l = mid +1
        else:
            idx = mid
            r = mid -1


    return idx


arr = [10,20,30,40,50,60,70]

print(peak_of_mountain_array(arr))

arr = [20,30,40,50,60,70,10]

print(peak_of_mountain_array(arr))

arr = [30,40,50,60,70,10,20]

print(peak_of_mountain_array(arr))

arr = [50,60,70,10,20,30,40]

print(peak_of_mountain_array(arr))

