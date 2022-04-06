import string
def rotationalCipher(input, rotational_factor):

    if not input or rotational_factor == 0:
        return input

    #input_list = input.split()
    #print('input list', input_list)
    character_rotation = {}
    output_list = []

    a_ascii = ord('a')
    A_ascii = ord('A')
    z_ascii = ord('z')
    Z_ascii = ord('Z')

    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    shifted_alphabet_lower = alphabet_lower[rotational_factor:] + alphabet_lower[:rotational_factor]
    shifted_alphabet_upper = alphabet_upper[rotational_factor:] + alphabet_upper[:rotational_factor]

    print('input ', input)

    for char in input:
        print('char', char)
        if char in character_rotation:
            output_list.append(character_rotation[char])

        elif char.isdigit():
            val = (int(char) + rotational_factor) % 10
            character_rotation[char] = str(val)
            output_list.append(character_rotation[char])

        elif char in string.ascii_lowercase:

            uni_val = ord(char)
            new_val = uni_val + rotational_factor
            '''if new_val > z_ascii:
                new_val = new_val - z_ascii +(a_ascii-1)'''

            print('inside ', a_ascii, z_ascii, char, uni_val, new_val, (new_val-(a_ascii-1)) % z_ascii, (new_val % z_ascii) + (a_ascii-1))

            if new_val > z_ascii:
                new_val = (uni_val + ( rotational_factor % 26)) + (a_ascii-1)

            val = chr(new_val)
            character_rotation[char] = val
            output_list.append(character_rotation[char])

        elif char in string.ascii_uppercase:
            uni_val = ord(char)
            new_val = uni_val + rotational_factor
            '''if new_val > Z_ascii:
                new_val = new_val - Z_ascii +(A_ascii-1)'''

            if new_val > Z_ascii:
                new_val = (new_val % 26) + (A_ascii-1)

            val = chr(new_val)
            character_rotation[char] = val
            output_list.append(character_rotation[char])

        else:
            character_rotation[char] = char
            output_list.append(character_rotation[char])

        #print('out char', char, character_rotation[char])

    return ''.join(output_list)


def printString(string):
    print('[\"', string, '\"]', sep='', end='')

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
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1

if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    print('out', output_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    print('out', output_2)
    check(expected_2, output_2)





