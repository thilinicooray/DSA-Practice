from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    unique_combo = []
    cur = []

    def dfs(i,sum):
        if sum == target:
            unique_combo.append(cur.copy())
            return

        for j in range(i,len(candidates)):
            if sum + candidates[j] <= target:
                cur.append(candidates[j])
                dfs(j, sum + candidates[j])
                cur.pop()

    dfs(0,0)
    return unique_combo


if __name__ == '__main__':
    candidates = [int(x) for x in '2 3 6 7'.split()]
    target = int('7')
    res = combination_sum(candidates, target)
    for row in res:
        print(' '.join(map(str, row)))