def longest_substring_without_repeating_characters(s: str) -> int:
    if not s:
        return 0

    if len(s) == 1:
        return 1

    l=0
    r = 0
    window = set()
    max_len = 0

    while r < len(s):
        if s[r] not in window:
            window.add(s[r])
            r += 1

        else:
            window.remove(s[l])
            l+= 1

        max_len = max(max_len, r-l)

    return  max_len

if __name__ == '__main__':
    s = 'abcdbea'
    res = longest_substring_without_repeating_characters(s)
    print(res)