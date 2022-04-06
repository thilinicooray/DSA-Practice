
def square_root(n: int) -> int:

    if n < 0:
        return -1

    if n == 0 :
        return n

    val = -1

    l = 1
    r = n

    while l <= r :
        mid = (l+r) //2

        cur = mid * mid

        if cur == n :
            return mid
        elif cur > n:
            r = mid
        else:
            if mid > val:
                l = mid
                val = l
            else:
                return val


print(square_root(0))
print(square_root(1))
print(square_root(3))
print(square_root(8))
print(square_root(16))

