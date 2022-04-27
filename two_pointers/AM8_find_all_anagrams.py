from typing import List

def find_all_anagrams(original: str, check: str) -> List[int]:
    from collections import Counter
    if not original or not check or (len(original) < len(check)):
        return []

    l = 0
    check_set = Counter(check)
    idx = []

    while (l + (len(check) - 1)) < len(original):
        r = l + len(check)

        cur_set = Counter(original[l:r])

        if cur_set == check_set:
            idx.append(l)
        l += 1

    return idx


if __name__ == '__main__':
    original = 'nabanabannaabbaanana'
    check = 'banana'
    res = find_all_anagrams(original, check)
    print(' '.join(map(str, res)))