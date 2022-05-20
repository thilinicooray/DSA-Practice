def get_sum_subarray(arr, target):
    if not arr:
        return [-1,-1]

    prefix_sum = {0:0}
    cur_sum = 0
    for i in range(len(arr)):
        val = arr[i]
        cur_sum += val
        remainder = cur_sum - target

        if remainder in prefix_sum:
            return [prefix_sum[remainder]-1, i+1]
        prefix_sum[cur_sum] = i+1


arr = [1,5,-3,7,9,2,-4,6]
target = 13

print('idx of subarray', get_sum_subarray(arr, target))