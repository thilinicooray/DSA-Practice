from typing import List

def move_zeros(nums: List[int]) -> None:
    if not nums:
        return

    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            tmp = nums[slow]
            nums[slow] = nums[fast]
            nums[fast] = tmp
            slow += 1

if __name__ == '__main__':
    nums = [int(x) for x in '1 0 2 0 0 7'.split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))
