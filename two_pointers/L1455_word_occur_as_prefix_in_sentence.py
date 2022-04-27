


def find_prefix(sent, word):


    s_words = sent.split()

    for i,w in enumerate(s_words):
        if len(w) < len(word):
            continue

        found = True
        for r in range(len(word)):
            if w[r] != word[r]:
                found = False
                break

        if found:
            return i +1

    return -1



print(find_prefix('this problem is an easy problem', 'pro'))