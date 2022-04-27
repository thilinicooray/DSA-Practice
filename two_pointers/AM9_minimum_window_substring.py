def get_minimum_window(original: str, check: str) -> str:
    from collections import Counter

    if not original or not check or (len(original) < len(check)):
        return ''

    check_ctr = Counter(check)
    l = 0
    min_len = len(original) +1
    best_l = -1
    best_r = -1
    r = l + (len(check) )

    def is_matching(l,r):
        cur = Counter(original[l:r])

        for char, c in check_ctr.items():
            if cur[char] < c:
                return False
        return True

    while r <= len(original):
        contains = is_matching(l,r)
        if contains:
            cur_len = r -l

            if cur_len < min_len:
                min_len = cur_len
                best_l = l
                best_r = r

            min_len = min(min_len, r -l)
            l += 1
        else:
            r += 1



    return original[best_l:best_r]



if __name__ == '__main__':
    original = 'abdcaghbaac'
    check = 'aabc'
    res = get_minimum_window(original, check)
    print(res)