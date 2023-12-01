import sys

letters = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def find_last_digit(s : str):
    last = (-1, -1)
    for i in range(len(s)):
        c = s[i]
        if c.isnumeric():
            last = (int(c), i)
    return last


def find_first_digit(s : str):
    for i in range(len(s)):
        c = s[i]
        if c.isnumeric():
            return (int(c), i)
    return (-1, -1)


def find_last_letter(s : str):
    last = (-1, -1)
    for i in range(len(letters)):
        ind = s.rfind(letters[i])
        if (ind == -1):
            continue
        if (last[1] < ind):
            last = (i + 1, ind)
    return last

def find_first_letter(s : str):
    first = (-1, -1)
    for i in range(len(letters)):
        ind = s.find(letters[i])
        if (ind == -1):
            continue
        if (first[1] == -1 or first[1] > ind):
            first = (i + 1, ind)
    return first
    

def find_first_and_last(s : str):
    digit_first = find_first_digit(s)
    digit_last = find_last_digit(s)
    letter_first = find_first_letter(s)
    letter_last = find_last_letter(s)
    print(f'first digit: {digit_first} last digit: {digit_last}')
    print(f'first letter: {letter_first} last letter: {letter_last}')
    first = digit_first[0] if digit_first[1] != -1 and (letter_first[1] == -1 or digit_first[1] < letter_first[1]) else letter_first[0]
    last = digit_last[0] if digit_last[1] != -1 and (letter_last[1] == -1 or digit_last[1] > letter_last[1]) else letter_last[0]
    together = first * 10 + last
    print(f'{s} -> {together}')
    return together




def main(argv, argc):
    total = 0
    for line in open(argv[1]).readlines():
        total += find_first_and_last(line)
    print(total)

    

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
