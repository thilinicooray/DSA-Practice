

def is_end_reachable_dynamic(jumps):
    can_jump = {len(jumps)-1 : True}

    def reach_forward(cur_index):

        if cur_index in can_jump:
            return can_jump[cur_index]

        max_jump = jumps[cur_index]
        can = False
        for i in range(1,max_jump+1):
            next_idx = cur_index + i

            if next_idx < len(jumps):
                can = can or reach_forward(next_idx)
        can_jump[cur_index] = can
        return can

    return reach_forward(0)

def is_end_reachable_greedy(jumps):
    last_idx = len(jumps) -1

    for i in range(len(jumps)-2,-1,-1):
        if i + jumps[i] >= last_idx:
            last_idx = i

    return last_idx == 0 


jumps = [2,3,1,1,4]

print(is_end_reachable_greedy(jumps))