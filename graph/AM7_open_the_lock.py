from typing import List

def num_steps(combo: str, trapped_combos: List[str]) -> int:

    def get_next_combos(cur):
        next_combos = set()

        for i in range(len(cur)):
            up_digit = str((int(cur[i]) + 1) % 10)
            next_combos.add(cur[:i] + up_digit + cur[i+1:])
            down_digit = str((int(cur[i]) -1 + 10) % 10)
            next_combos.add(cur[:i] + down_digit + cur[i+1:])

        return next_combos

    from collections import deque
    q = deque([('0000', 0)])
    visited = set(trapped_combos)
    visited.add('0000')
    while q:
        cur_combo, steps = q.popleft()

        if cur_combo == combo:
            return steps

        next_combos = get_next_combos(cur_combo)

        for next_c in next_combos:
            if next_c not in visited:
                q.append((next_c, steps + 1))
                visited.add(next_c)

    return -1


if __name__ == '__main__':
    combo = input()
    trapped_combos = input().split()
    res = num_steps(combo, trapped_combos)
    print(res)
