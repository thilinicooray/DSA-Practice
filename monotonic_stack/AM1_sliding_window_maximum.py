

def get_sliding_window_max(arr,k):
    if len(arr) < k:
        return [max(arr)]

    l = 0
    r = k -1
    res = []
    from collections import deque
    q = deque()

    while r < len(arr):

        while q and arr[q[-1]] <= arr[l]:
            q.pop()

        q.append(l)

        if l == r:
            res.append(arr[q[0]])
            r += 1
            if q[0] < (r - k + 1):
                q.popleft()

        l += 1


    return res

arr = [1, 3, 2, 5, 8, 7]
k = 3

print(get_sliding_window_max(arr,k))