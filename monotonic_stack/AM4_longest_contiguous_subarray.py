
def get_max_subarray_len(nums, limit):
    if not nums:
        return -1

    from collections import deque
    min_q = deque()
    max_q = deque()

    longest_len = 0
    start = 0

    for end in range(len(nums)):
        while min_q and nums[min_q[-1]] > nums[end]:
            min_q.pop()
        min_q.append(end)

        while max_q and nums[max_q[-1]] < nums[end]:
            max_q.pop()
        max_q.append(end)

        while nums[max_q[0]] - nums[min_q[0]] > limit:
            if max_q[0] == start:
                max_q.popleft()
            if min_q[0] == start:
                min_q.popleft()

            start += 1

        longest_len = max(longest_len, end - start + 1)

    return longest_len

from collections import deque
from typing import List
def longest_subarray(nums: List[int], limit: int) -> int:
    best = 0
    # A strictly increasing deque consisting of members from [left, right]
    # The min item in this subarray is min_deque[0]
    min_deque = deque()
    # A strictly decreasing deque consisting of members from [left, right]
    # The max item in this subarray is max_deque[0]
    max_deque = deque()
    left = 0
    n = len(nums)
    for right in range(n):
        while min_deque and nums[right] < nums[min_deque[-1]]:
            min_deque.pop()
        min_deque.append(right)
        while max_deque and nums[right] > nums[max_deque[-1]]:
            max_deque.pop()
        max_deque.append(right)
        # While the amplitude exceeds `limit`, increasing `left` and popping
        # items if needed
        while nums[max_deque[0]] - nums[min_deque[0]] > limit:
            if max_deque[0] == left:
                max_deque.popleft()
            if min_deque[0] == left:
                min_deque.popleft()
            left += 1
        # Stores the max subarray size up to this point
        best = max(best, right - left + 1)
    return best

nums = [7, 14, 10, 5, 10, 6, 3, 6, 5, 5, 9, 13]
limit = 5

print(get_max_subarray_len(nums, limit))