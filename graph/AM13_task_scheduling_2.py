from collections import deque

def get_task_time_dict(tasks, times):
    task_time = {}

    for i, task in enumerate(tasks):
        task_time[task] = times[i]

    return task_time

def get_dependents(tasks, reqs):
    dep = {}
    dep_counts = {}

    for req in reqs:
        for i in range(len(req)):

            if req[i] not in dep:
                dep[req[i]] = set()

            if req[i] not in dep_counts:
                dep_counts[req[i]] = 0

            if i > 0:
                cur = req[i]
                prev = req[i-1]

                if cur not in dep[prev]:
                    dep[prev].add(cur)
                    dep_counts[cur] +=1

    for task in tasks:
        if task not in dep:
            dep[task] = set()

        if task not in dep_counts:
            dep_counts[task] = 0

    return dep, dep_counts


def min_time_for_task_completion(tasks, times, requirements):
    task_time_dict = get_task_time_dict(tasks, times)
    dep, dep_counts = get_dependents(tasks, requirements)

    q = deque()
    min_time = 0
    item_comp_times = {}

    for k,v in dep_counts.items():
        if v == 0:
            q.append(k)
            item_comp_times[k] = task_time_dict[k]
            min_time = max(min_time, item_comp_times[k])
        else:
            item_comp_times[k] = 0

    while q:
        item = q.popleft()

        children = dep[item]

        for child in children:
            item_comp_times[child] = max(item_comp_times[child], item_comp_times[item] + task_time_dict[child])
            min_time = max(min_time, item_comp_times[child])
            dep_counts[child] -= 1

            if dep_counts[child] == 0:
                q.append(child)

    return min_time





tasks = ["a", "b", "c", "d"]
times = [1, 1, 2, 1]
requirements = [["a", "b"], ["c", "b"], ["b", "d"]]

print(min_time_for_task_completion(tasks, times, requirements))