
def get_max_rain_water_trapped(cols):
    left_boundaries = [0] * len(cols)
    right_boundaries = [0] * len(cols)

    max_left = 0

    for i in range(len(cols)):
        left_boundaries[i] = max_left
        max_left = max(max_left, cols[i])

    max_right = 0

    for i in range(len(cols)-1,-1,-1):
        right_boundaries[i] = max_right
        max_right = max(max_right, cols[i])

    trapped_water = 0

    for i in range(len(cols)):
        min_boundary = min(left_boundaries[i], right_boundaries[i])
        if min_boundary > cols[i]:
            trapped_water += (min_boundary - cols[i])

    return trapped_water

cols = [2,1,1,2,3]

print('max rainwater trapped is {}'.format(get_max_rain_water_trapped(cols)))