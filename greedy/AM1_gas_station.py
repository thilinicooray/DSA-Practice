
def get_starting_position(gas, dist):
    if sum(gas) < sum(dist):
        return -1

    total = 0
    start = 0

    for i in range(len(gas)):
        total += (gas[i] - dist[i])

        if total < 0:
            total = 0
            start = i+1

    return start


gas = [1, 2, 3, 4, 5]
dist = [3, 4, 5, 1, 2]

print('starting point for a round trip is {}'.format(get_starting_position(gas, dist)))