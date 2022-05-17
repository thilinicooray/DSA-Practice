from collections import deque

def get_dependents(seqs):
    dep = {}
    dep_counts = {}

    for seq in seqs:
        for i in range(len(seq)):
            if seq[i] not in dep:
                dep[seq[i]] = set()

            if seq[i] not in dep_counts:
                dep_counts[seq[i]] = 0

            if i >0:
                prev = seq[i-1]
                cur = seq[i]

                if cur not in dep[prev]:
                    dep[prev].add(cur)
                    dep_counts[cur] += 1

    return dep, dep_counts

def is_original_unique(original, seqs):

    dep, dep_counts = get_dependents(seqs)
    print(dep, dep_counts)
    q = deque()
    seq = []

    for k,v in dep_counts.items():
        if v == 0:
            q.append(k)

    while q:
        if len(q) > 1:
            return False

        item = q.popleft()
        seq.append(item)
        children = dep[item]

        for child in children:
            dep_counts[child] -= 1

            if dep_counts[child] == 0:
                q.append(child)

    return True if seq == original else False


original  = [4,1,5,2,6,3]
seqs = [[5,2,6,3], [4,1,5,2]]

print(is_original_unique(original, seqs))