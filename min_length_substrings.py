import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def substring_match(s, dict, len):
    min = -1
    max = 0
    len1 = len
    dict1 = dict
    for i,char in enumerate(s):
        if char in dict1 and dict1[char] != 0:
            dict1[char] -= 1
            len1 -=1

            if min == -1:
                min == i

            if len1 == 0:
                max = i
                break

    return -1 if len1 > 0 else max -min





def min_length_substring(s, t):
    s= list(s)
    t = list(t)

    dict = {}

    for char in t :
        if char not in dict:
            dict[char] = 0

        dict[char] +=1

    min_len = len(s) *2
    len_t = len(t)



    for i in range(len(s)):
        len1 = substring_match(s[i:], dict, len_t)


        if len1 != -1 and len1 < min_len:
            min_len  = len1

    return -1 if min_len == len(s) *2 else min_len













# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
    print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
        printInteger(expected)
        print(' Your output: ', end='')
        printInteger(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    s1 = "dcbefebce"
    t1 = "fd"
    expected_1 = 5
    output_1 = min_length_substring(s1, t1)
    check(expected_1, output_1)

    s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
    t2 = "cbccfafebccdccebdd"
    expected_2 = -1
    output_2 = min_length_substring(s2, t2)
    check(expected_2, output_2)

    # Add your own test cases here
