


def get_subarray_min_wrong(arr):
    stack = []
    min_sum = 0

    for i in range(len(arr)):
        start = i
        while stack and stack[-1][1] > arr[i]:
            print('inside',stack,i)
            start_idx, val = stack.pop()
            min_sum += val*(i-start_idx)
            print(val, i-start_idx)
            start = start_idx

        stack.append((start,arr[i]))
    print(stack)

    while stack:
        start_idx, val = stack.pop()
        min_sum += val*(len(arr) - start_idx)
        print(val, len(arr)-start_idx)

    return min_sum

def get_subarray_min(arr):
    min_sum = 0
    for i in range(len(arr)):
        stack = []
        cur = arr[:i+1]
        for j in range(len(cur)-1, -1, -1):
            while stack and stack[-1] > cur[j]:
                stack.pop()
            stack.append(cur[j])
            print(stack)
            min_sum += stack[0]

    return min_sum





arr = [1,2,3]
arr1 = [1,5,3,4,2,5]

print(get_subarray_min(arr1))