
from typing import List

def word_break(s: str, words: List[str]) -> bool:
    if not s:
        return False

    possible_prefix = {}

    def dfs(cur):


        if cur in possible_prefix:
            return possible_prefix[cur]

        if cur == s:
            return True



        possible_prefix[cur] = cur == s[:len(cur)]

        

        if cur not in possible_prefix or possible_prefix[cur]

        for w in words:
            cur.append(w)


            dfs(cur)
            cur.pop()

