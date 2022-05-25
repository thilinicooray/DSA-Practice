
def get_closest_values(arr,k,x):
    from collections import deque
    closest = deque()
    l = 0
    r = l

    while r < len(arr):
        if len(closest) < k:
            closest.append(arr[r])
            r += 1

        else:
            if abs(closest[0] -x) > abs(arr[r] - x):
                closest.popleft()
                closest.append(arr[r])
            else:
                break

    return list(closest)

def get_closest_values_binary_search(arr,k,x):
    l=0
    r = len(arr)-1

    while l < r:
        m = (l+r) // 2
        if abs(arr[m] -x) < abs(arr[m+k]-x):
            r = m
        else:
            l = m+1

    return arr[l:l+k]

arr = [1,2,3,4,5,6]
k = 3
x=3

print(get_closest_values_binary_search(arr,k,x))