from collections import deque

def count_nice_sub_arrays(arr,k):
    if not arr or not k or len(arr) < k:
        return 0

    left = -1
    count = 0
    odd_ele = deque()
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            odd_ele.append(i)

        if len(odd_ele) == k:
            count += odd_ele[0] - left

        if len(odd_ele) > k:
            left = odd_ele.popleft()
            count += odd_ele[0] - left

    return count


input_array = [2, 4, 5, 7, 8, 10, 11, 12, 14, 15, 18, 20]
k = 3

print('num of nice subarrays is {}'.format(count_nice_sub_arrays(input_array,k)))