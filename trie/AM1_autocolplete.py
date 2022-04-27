from typing import List

class Node:
    def __init__(self):
        self.children = {}
        self.eow = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        cur = self.root

        for w in word:
            if w not in cur.children:
                cur.children[w] = Node()

            cur = cur.children[w]

        cur.eow = True

    def min_strokes_to_find(self, word):
        cur = self.root
        min_strokes = 1

        for w in word:
            if w not in cur.children:
                return -1
            else:
                if len(cur.children) == 1:
                    return min_strokes

            min_strokes += 1
            cur = cur.children[w]

        return min_strokes


def autocomplete(words: List[str]) -> int:
    if not words:
        return 0

    t = Trie()
    min_strokes = 0

    for word in words:
        t.insert(word)
        min_strokes += t.min_strokes_to_find(word)
        print('min ', word, min_strokes)

    return min_strokes



if __name__ == '__main__':
    words = 'hi hello bojack hills hill'.split()
    res = autocomplete(words)
    print(res)