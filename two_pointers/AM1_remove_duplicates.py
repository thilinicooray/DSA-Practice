from typing import List

def remove_duplicates(arr: List[int]) -> int:
    if not arr:
        return -1

    l = 0
    r = l+1

    while r < len(arr):
        if arr[r] != arr[l]:
            l +=1
            tmp = arr[l]
            arr[l] = arr[r]
            arr[r] = tmp
        r += 1

    return l+1


if __name__ == '__main__':
    arr = [int(x) for x in '1 1 1 2'.split()]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))