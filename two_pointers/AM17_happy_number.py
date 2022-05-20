
def next(n):
    res = 0

    while n > 0:
        res += n%10
        n = n//10

    return res

def is_this_happy_opt(number):

    slow = next(number)
    fast = next(slow)

    while fast!= 1 and slow != fast:

        slow = next(slow)
        fast = next(next(fast))

    return fast == 1


def is_this_happy(number):

    if number == 1:
        return True

    visited = set()
    visited.add(number)
    while number:
        st_num = str(number)
        number = 0

        for char in st_num:
            number += int(char) ** 2

        if number == 1:
            return True
        if number in visited:
            return False

        visited.add(number)

number = 19

print(is_this_happy_opt(number))