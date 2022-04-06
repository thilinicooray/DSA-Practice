class Solution:
    def reverseWords(self, s: str) -> str:
        s = str.strip(s)
        s_list = s.split()

        new = []

        for i in range(len(s_list)-1,-1,-1):
            new.append(s_list[i])

        return ' '.join(new)

        '''reversed = ''
        cur = ''

        for i in range(len(s)-1,-1,-1):
            char = s[i]
            if char == ' ' :
                if cur == '':
                    continue
                else:
                    reversed = reversed + ' ' + cur
                    cur = ''

            else:
                cur = char + cur

        return (reversed + ' ' + cur)[1:]'''




        '''reversed = ''

        for i in range(len(s)-1,-1,-1):
            char = s[i]
            if char == ' ' and char == reversed[-1]:
                continue

            reversed += char


        return reversed'''


s = Solution()

print(s.reverseWords('   hello   kitty '))



