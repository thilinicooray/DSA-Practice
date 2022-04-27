from typing import List

def triplets_with_sum_0(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []

    nums.sort()
    sums = []
    for i, a in enumerate(nums):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i+1
        r = len(nums) -1

        while l <r:
            three_sum = a + nums[l] + nums[r]

            if three_sum < 0:
                l += 1
            elif three_sum > 0:
                r -= 1
            else:
                sums.append([a, nums[l], nums[r]])
                l +=1

                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return sums

if __name__ == '__main__':
    nums = [int(x) for x in '1 -1 2 -2 3 -3 4 -4'.split()]
    res = triplets_with_sum_0(nums)
    for row in res:
        print(' '.join(map(str, row)))