
from typing import List

def word_break(s: str, words: List[str]) -> bool:
    if not s:
        return False

    breakable = [False] * (len(s)+1)
    breakable[-1] = True

    for i in range(len(s) -1, -1, -1):
        for w in words:
            if (i+len(w)) <= len(s) and s[i : (i+len(w))] == w:
                print(i, w)
                breakable[i] = breakable[i+len(w)]

            if breakable[i]:
                break

    return breakable[0]

print(word_break('catsittree',['cats','cat','sit', 'tree']))
