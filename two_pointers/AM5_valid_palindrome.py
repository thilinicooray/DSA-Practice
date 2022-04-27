def is_palindrome(s: str) -> bool:
    if not s:
        return True

    l = 0
    r = len(s) -1

    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l< r and not s[r].isalnum():
            r -= 1

        lower_l = s[l].lower()
        lower_r = s[r].lower()

        if lower_l != lower_r:
            return False

        l += 1
        r -= 1

    return True


if __name__ == '__main__':
    s = 'Do geese see God??????'
    res = is_palindrome(s)
    print('true' if res else 'false')