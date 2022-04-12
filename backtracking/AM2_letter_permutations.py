from typing import List

def permutations(letters: str) -> List[str]:
    if not letters:
        return []

    combo = []
    org_list = list(letters)

    def perm(str_l):

        if len(str_l) == len(org_list):
            combo.append(''.join(str_l))

        for char in org_list:
            if char not in str_l:
                str_l.append(char)
                perm(str_l)
                str_l.pop()


    perm([])

    return combo

print(permutations('abcd'))