from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    if not nums:
        return []

    powerset = []
    powerset.append([])
    cur = []

    def dfs(i):
        if i >= len(nums):
            return

        for j in range(i, len(nums)):
            cur.append(nums[j])
            powerset.append(cur.copy())
            dfs(j+1)
            cur.pop()

    dfs(0)

    return powerset

if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    res = subsets(nums)
    res = [' '.join(str(x) for x in sorted(subset)) for subset in res]
    res.sort()
    for row in res:
        print(row)