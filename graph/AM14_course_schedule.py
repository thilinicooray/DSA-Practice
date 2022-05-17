from collections import deque

def get_dependents(pre_req):
    dep = {}
    dep_counts = {}

    for seq in pre_req:
        for i in range(len(seq)):
            if seq[i] not in dep:
                dep[seq[i]] = set()
            if seq[i] not in dep_counts:
                dep_counts[seq[i]] = 0

            if i >0:
                cur = seq[i]
                dependee = seq[i-1]

                if dependee not in dep[cur]:
                    dep[cur].add(dependee)
                    dep_counts[dependee] +=1

    return dep, dep_counts

def is_valid_course_schedule(n, pre_req):
    dep, dep_counts = get_dependents(pre_req)
    q = deque()

    for k,v in dep_counts.items():
        if v == 0:
            q.append(k)

    while q:
        item = q.popleft()
        children = dep[item]

        for child in children:
            dep_counts[child] -= 1

            if dep_counts[child] == 0:
                q.append(child)

    completed_count = 0

    for k,v in dep_counts.items():
        if v == 0:
            completed_count += 1

    return completed_count == n

pre_req = [[0,1],[2,3]]
n = 4

print(is_valid_course_schedule(n, pre_req))