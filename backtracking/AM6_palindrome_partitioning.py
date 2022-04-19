from typing import List

def partition(s: str) -> List[List[str]]:
    all = []
    cur = []

    def is_palindrome(s, l, r):
        while l<r:
            if s[l] != s[r]:
                return False
            l = l+1
            r = r -1

        return True


    def dfs(i):
        if i == len(s):
            all.append(cur.copy())
            return

        for j in range(i,len(s)):
            if is_palindrome(s, i,j):
                cur.append(s[i:j+1])
                dfs(j+1)
                cur.pop()

    dfs(0)
    return all

if __name__ == '__main__':
    s = input()
    res = partition('aaabab')
    for row in res:
        print(' '.join(row))