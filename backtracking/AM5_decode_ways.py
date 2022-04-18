


def decode_ways(digits: str) -> int:


    decoded = {}

    def dfs(i):

        if i == len(digits):
            return 1

        if i in decoded:
            return decoded[i]

        count = 0
        if digits[i] != '0':
            count += dfs(i+1)

        if i+2 <= len(digits) and 0 < int(digits[i:i+2]) < 27:
            count += dfs(i+2)

        decoded[i] = count

        return decoded[i]

    return dfs(0)





print(decode_ways('110'))