

def is_isomorphic(str_1: str, str_2: str) -> bool:

    if len(str_1) != len(str_2):
        return False

    mapping21= {}
    used = set()


    for i,e in enumerate(str_1):
        match = str_2[i]

        if e in mapping21 :
            if mapping21[e] != match:
                return False

        else:
            if match in used:
                return False

            mapping21[e] = match
            used.add(match)


    return True


str1 = 'wow'
str2 = 'gog'

print(is_isomorphic(str1,str2))

str1 = 'aab'
str2 = 'gcn'

print(is_isomorphic(str1,str2))

