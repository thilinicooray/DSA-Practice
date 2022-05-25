
def get_size_of_largest_rect(heights):

    max_size = 0
    stack = []
    for i in range(len(heights)):
        pop_count = 0
        while stack and stack[-1][1] > heights[i]:
            idx, val = stack.pop()
            max_size = max(max_size, val*(i-idx))
            pop_count+=1
        stack.append((i-pop_count,heights[i]))

    while stack:
        idx, val =  stack.pop()
        max_size = max(max_size, val*(len(heights)-idx))

    return max_size



heights = [1,2,2,3,2,4,2,1,2]
#heights = [2,1,5,6,2,3]

print(get_size_of_largest_rect(heights))