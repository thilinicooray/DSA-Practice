



class Solution:
    def generateParenthesis(self, n):

        res = []
        stack = []

        def rec_paranthesis_gen(open_count, closed_count, stack):
            if open_count == closed_count == n:
                res.append(''.join(stack))
                return

            if open_count < n:
                stack.append('(')
                rec_paranthesis_gen(open_count+1, closed_count, stack)
                stack.pop()

            if closed_count < open_count:
                stack.append(')')
                rec_paranthesis_gen(open_count, closed_count+1, stack)
                stack.pop()

        rec_paranthesis_gen(0,0,stack)

        return res

s = Solution()

print(s.generateParenthesis(3))
