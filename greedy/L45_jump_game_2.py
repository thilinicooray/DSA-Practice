
def get_min_steps_greedy(jumps):
    steps = 0
    l = r= 0

    while r < len(jumps) - 1:
        farthest = 0
        for i in range(l,r+1):
            farthest = max(farthest, i + jumps[i])

        l = r+1
        r = farthest
        steps += 1

    return steps

def get_min_steps(jumps):

    if not jumps or len((jumps)) == 1 :
        return 0

    from collections import deque
    q = deque([(0,0)])

    while q:
        cur_idx,step = q.popleft()

        max_step = jumps[cur_idx]

        for j in range(1,1+max_step):
            i  = cur_idx + j
            if i == len(jumps) - 1:
                return step + 1

            if i < len(jumps) - 1:
                q.append((i,step+1))

def get_min_steps_dynamic(jumps):
    can_jump = {len(jumps)-1 : 0}

    def reach_forward(cur_index):

        if cur_index in can_jump:
            return can_jump[cur_index]

        max_jump = jumps[cur_index]
        min_steps = len(jumps)
        for i in range(1,max_jump+1):
            next_idx = cur_index + i

            if next_idx < len(jumps):
                min_steps = min(min_steps,1 + reach_forward(next_idx))
        can_jump[cur_index] = min_steps
        return can_jump[cur_index]

    return reach_forward(0)

jumps = [1,2,1,1,1]

print('min steps to reach the end is {}'.format(get_min_steps_greedy(jumps)))