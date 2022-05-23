
def get_waiting_days(temp):
    if not temp:
        return [-1]

    stack = []
    waiting_days = [0]* len(temp)

    for i in range(len(temp)):
        while stack and temp[stack[-1]] < temp[i]:
            idx = stack.pop()
            waiting_days[idx] = (i - idx)

        stack.append(i)

    return waiting_days


temp = [73, 74, 75, 71, 69, 72, 76, 73]

print(get_waiting_days(temp))