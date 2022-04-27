from typing import List

def count_nice_subarrays(k: int, arr: List[int]) -> int:

    from collections import deque

    if not arr or k <= 0 or len(arr) < k:
        return 0

    l = -1

    n_sub = 0
    odd_idx = deque()

    for r in range(len(arr)):
        if arr[r] %2 != 0:
            odd_idx.append(r)

        if len(odd_idx) == k:
            n_sub += odd_idx[0] - l

        elif len(odd_idx) > k:
            l = odd_idx.popleft()
            n_sub += odd_idx[0] - l

    return n_sub


if __name__ == '__main__':
    k = int(3)
    arr = [int(x) for x in '1 1 2 1 1 2'.split()]
    res = count_nice_subarrays(k, arr)
    print(res)