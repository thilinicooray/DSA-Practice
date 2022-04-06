
from collections import Counter
from typing import List

def group_anagrams(strs):
    ana_map = {}

    for st in strs:
        #ct= Counter(st)
        ct = "".join(sorted(st))

        if ct not in ana_map:
            ana_map[ct] = []

        ana_map[ct].append(st)

    ana_group = []

    for k,v in ana_map.items():
        v.sort()
        ana_group.append(v)


    return ana_group



strs= ["eat" ,"tea", "tan", "ate", "nat", "bat"]


print(group_anagrams(strs))
