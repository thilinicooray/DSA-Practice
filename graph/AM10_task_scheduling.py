from collections import deque

def get_dependent_count(requirements):
    dep = {}
    dep_counts = {}

    for task_order in requirements:
        for i in range(len(task_order)):

            if task_order[i] not in dep:
                dep[task_order[i]] = []

            if task_order[i] not in dep_counts:
                dep_counts[task_order[i]] = 0


            if i > 0:
                prev_task = task_order[i-1]
                cur_task = task_order[i]

                dep[prev_task].append(cur_task)
                dep_counts[cur_task] += 1

    return dep_counts, dep




def get_task_performing_sequence(tasks, requirements):
    dependent_counts, dependents = get_dependent_count(requirements)
    print(dependent_counts, dependents)
    q = deque()
    seq = []

    for k,v in dependent_counts.items():
        if v == 0:
            q.append(k)

    while q:
        task = q.popleft()
        seq.append(task)

        children = dependents[task]

        for child in children:
            dependent_counts[child] -= 1
            if dependent_counts[child] == 0:
                q.append(child)

    return seq

tasks = ['abbreviate', 'bricks', 'cardinals', 'dextrous', 'fibre', 'green', 'height']
requirements = [['abbreviate', 'bricks'], ['cardinals', 'bricks'], ['dextrous', 'bricks'], ['bricks', 'fibre'], ['green', 'fibre']]

print(get_task_performing_sequence(tasks, requirements))