
def get_next_greater_element(arr):
    if not arr:
        return -1

    res = [-1]*len(arr)
    stack = []

    for i in range(len(arr)):
        while stack  and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            res[idx] = arr[i]
        stack.append(i)

    for i in range(len(arr)):
        while stack  and arr[stack[-1]] < arr[i]:
            idx = stack.pop()
            res[idx] = arr[i]

    return res




arr = [1,2,1]

print(get_next_greater_element(arr))