from collections import Counter
def get_num_subarrays_div_by_k(arr,k):
    prefix_modulo = Counter()
    prefix_modulo[0] = 1

    cur_sum = 0
    count = 0

    for ele in arr:
        cur_sum += ele
        modulo = cur_sum % k
        remainder = (k-modulo) % k

        if remainder in prefix_modulo:
            count += prefix_modulo[remainder]

        prefix_modulo[remainder] += 1

    return count

arr = [1,2,1,1,5,-3,4,1]
k = 5

print('number of subarrays whose sums are div by {} is {}'.format(k, get_num_subarrays_div_by_k(arr,k)))