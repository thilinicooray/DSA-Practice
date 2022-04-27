from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    if not arr:
        return []

    l = 0
    r = len(arr) -1

    while l < r:
        two_sum = arr[l] + arr[r]
        if two_sum == target:
            return [l,r]
        elif two_sum > target:
            r -= 1
        else:
            l += 1


    return []

if __name__ == '__main__':
    arr = [int(x) for x in '1 4 5 8 11 13'.split()]
    target = int('10')
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))