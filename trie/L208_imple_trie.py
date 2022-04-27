
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

    def search(self, word):
        cur = self.root

        for w in word:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        return cur.eow

    def startswith(self, prefix):
        cur = self.root

        for w in prefix:
            if w not in cur.children:
                return False
            cur = cur.children[w]

        return True