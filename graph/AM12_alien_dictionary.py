import heapq

def get_seqs(words):
    seqs = []
    for j in range(1,len(words)):
        w1 = list(words[j-1])
        w2 = list(words[j])

        for i in range(len(w1)):
            if len(w2) > i and w1[i] != w2[i]:
                if [w1[i],w2[i]] not in seqs:
                    seqs.append([w1[i],w2[i]])

                break

    return seqs

def get_dependents(seqs, words):
    dep = {}
    dep_counts = {}

    for seq in seqs:
        for i in range(2):
            if seq[i] not in dep:
                dep[seq[i]] = set()
            if seq[i] not in dep_counts:
                dep_counts[seq[i]] = 0

            if i > 0:
                cur = seq[i]
                prev = seq[i-1]

                if cur not in dep[prev]:
                    dep[prev].add(cur)
                    dep_counts[cur] +=1

    for word in words:
        for i in range(len(word)):
            if word[i] not in dep:
                dep[word[i]] = set()
            if word[i] not in dep_counts:
                dep_counts[word[i]] = 0



    return dep, dep_counts

def letter_order(words):
    seqs = get_seqs(words)
    dep, dep_counts = get_dependents(seqs, words)

    print(seqs, dep, dep_counts)

    seq = []
    hp = []

    for k,v in dep_counts.items():
        if v == 0:
            heapq.heappush(hp,k)

    while hp:
        item = heapq.heappop(hp)

        seq.append(item)
        children = dep[item]

        for child in children:
            dep_counts[child] -= 1

            if dep_counts[child] == 0:
                heapq.heappush(hp, child)

    for k,v in dep_counts.items():
        if v != 0:
            return ''

    return ''.join(seq)





words = ["she","sell","seashell","seashore","seahorse","on","a"]

print(letter_order(words))