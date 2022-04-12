from typing import List

def letter_combinations_of_phone_number(digits: str) -> List[str]:

    if not digits:
        return []

    num_dict = {'2' : ['a','b','c'],'3':['d','e','f'],'4' :['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
                '7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']}

    #nums = list(digits)
    combo = []

    def dfs(cur):

        if len(cur) == len(digits):
            combo.append(''.join(cur))
            return

        cur_letters = num_dict[digits[len(cur)]]

        for char in cur_letters:
            cur.append(char)
            dfs(cur)
            cur.pop()

    dfs([])

    return combo

print(letter_combinations_of_phone_number('56'))