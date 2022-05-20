from collections import Counter
def get_subarray_sum_count(arr,target):
    prefix_sum = Counter()
    prefix_sum[0] = 1

    cur_sum = 0
    count = 0
    for ele in arr:
        cur_sum += ele
        remainder = cur_sum - target

        if remainder in prefix_sum:
            count += prefix_sum[remainder]

        prefix_sum[cur_sum] += 1

    return count

arr = [1,2,-5,2,1,3,1,1]
target = 2

print('number of times sub array sum was {} is {}'.format(target, get_subarray_sum_count(arr,target)))