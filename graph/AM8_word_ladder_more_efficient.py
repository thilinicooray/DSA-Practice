from collections import deque
from string import ascii_letters

def get_word_pattern_dict(word_list):
    patterns_dict = {}

    for word in word_list:
        for i in range(len(word)):
            cur_pattern = word[:i] + '*' +word[i+1:]

            if cur_pattern not in patterns_dict:
                patterns_dict[cur_pattern] = []

            patterns_dict[cur_pattern].append(word)

    '''
    ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]
    
    dict = {*OLD:[COLD, GOLD, SOLD], C*LD:[COLD], CO*D:[COLD, CORD], COL*:[COLD],
            G*LD:[GOLD], GO*D:[GOLD], GOL*:[GOLD], *ORD:[CORD], C*RD:[CORD, CARD],
            COR*:[CORD], S*LD:[SOLD], SO*D:[SOLD], SOL*:[SOLD], *ARD:[CARD, WARD, TARD], CA*D:[CARD], 
            CAR*:[CARD], W*RD:[WARD], WA*D:[WARD], WAR*:[WARD, WARM], *ARM:[WARM], W*RM:[WARM], 
            WA*M:[WARM], T*RD:[TARD], TA*D:[TARD], TAR*:[TARD]}
    
    '''

    return patterns_dict

def get_min_word_ladder_steps(start, end, word_list):

    if not word_list or end not in word_list:
        return -1

    #pattern_dict = get_word_pattern_dict(word_list)
    '''
    dict = {*OLD:[COLD, GOLD, SOLD], C*LD:[COLD], CO*D:[COLD, CORD], COL*:[COLD],
            G*LD:[GOLD], GO*D:[GOLD], GOL*:[GOLD], *ORD:[CORD], C*RD:[CORD, CARD],
            COR*:[CORD], S*LD:[SOLD], SO*D:[SOLD], SOL*:[SOLD], *ARD:[CARD, WARD, TARD], CA*D:[CARD], 
            CAR*:[CARD], W*RD:[WARD], WA*D:[WARD], WAR*:[WARD, WARM], *ARM:[WARM], W*RM:[WARM], 
            WA*M:[WARM], T*RD:[TARD], TA*D:[TARD], TAR*:[TARD]}
    
    '''

    q = deque([(start,0)])
    visited = set(start)

    def get_next_words(word):
        next_words = []

        '''
        TARD : *ARD, T*RD, TA*D, TAR*
        '''

        for i in range(len(word)):

            for c in ascii_letters:
                w = word[:i] + c +word[i+1:]
    
                if w not in word_list:
                    continue


                if w != word and w not in next_words and w not in visited:
                        next_words.append(w)

        return next_words


    '''
    q = [WARM-4]
    visited = (COLD-0, GOLD-1, SOLD-1, CORD-1, CARD-2, WARD-3, TARD-3)
    step = 1
    next_words = []
    '''
    while q:
        word, step = q.popleft()

        if word == end:
            return step

        next_words = get_next_words(word)

        for w in next_words:
            q.append((w, step+1))
            visited.add(w)

    return -1

start = 'hit'
end = 'cog'
word_list = ["hot","dot","dog","lot","log","cog"]

print('min steps from {} to {} is {}'.format(start, end, get_min_word_ladder_steps(start, end, word_list)))

'''
test case 1

start = 'hit'
end = 'cog'
word_list = ["COLD", "GOLD", "CORD", "SOLD", "CARD", "WARD", "WARM", "TARD"]

pattern_dict = {}

'''