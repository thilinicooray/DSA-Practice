


class Solution:
    def isValid(self, s: str) -> bool:
        para_dict = {'{':'}', '}':'{', '(':')', ')':'(','[':']', ']':'['}

        stack = []

        for char in s:
            if char not in ['}', ']', ')']:
                stack.append(char)

            else:
                if not stack:
                    return False

                out = stack.pop()

                if out != para_dict[char]:
                    return False

        return True if len(stack) == 0 else False


s = Solution()

print(s.isValid("[{}]"))
print(s.isValid("[{}]()"))
print(s.isValid("[{}]("))

