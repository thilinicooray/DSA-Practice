
def get_max_sbarray_minproduct(nums):
    prefix_sum = [0]

    for i,n in enumerate(nums):
        prefix_sum.append(n + prefix_sum[-1])

    stack = []
    max_prod = 0
    for i in range(len(nums)):
        start = i
        while stack and stack[-1][1] > nums[i]:
            idx, val = stack.pop()
            prod = val * (prefix_sum[i] - prefix_sum[idx])
            max_prod = max(max_prod, prod)
            start = idx

        stack.append((start, nums[i]))

    while stack:
        idx, val = stack.pop()
        prod = val * (prefix_sum[-1] - prefix_sum[idx])
        max_prod = max(max_prod, prod)

    return max_prod

nums = [1,2,3,2]

print('maximum subarray min-product is : {}'.format(get_max_sbarray_minproduct(nums)))