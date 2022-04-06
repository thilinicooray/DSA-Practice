

'''
test:
k_2 = 6
arr_2 = [1, 5, 3, 3, 3]

num_dict = {1:1,5:1,3:3}
pair_count = 1

sum_pairs = ((1,5))


'''
def numberOfWays(nums, k):

    if not nums or not k:
        return 0

    num_dict = {}
    for i,num in enumerate(nums):
        if num not in num_dict:
            num_dict[num] = []

        num_dict[num].append(i)

    print('num dict',num_dict)

    pair_count = 0

    sum_pairs = set()

    for i,num in enumerate(nums):
        remain = k - num

        if remain in num_dict:

            idxs = num_dict[remain]

            for j in idxs:
                if j != i and (i,j) not in sum_pairs and (j,i) not in sum_pairs:
                    pair_count +=1
                    sum_pairs.add((i,j))




    return pair_count


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
    k_1 = 6
    arr_1 = [1, 2, 3, 4, 3]
    expected_1 = 2
    output_1 = numberOfWays(arr_1, k_1)
    check(expected_1, output_1)

    k_2 = 6
    arr_2 = [1, 5, 3, 3, 3]
    expected_2 = 4
    output_2 = numberOfWays(arr_2, k_2)
    check(expected_2, output_2)
