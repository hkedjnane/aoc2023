import sys

def find_first_digit(s : str):
    for c in s:
        if c.isnumeric():
            return int(c)


def main(argv, argc):
    total = 0
    for line in open(argv[1]).readlines():
        first = find_first_digit(line)
        last = find_first_digit(line[::-1])
        together = first * 10 + last
        print(f'{line} -> {together}')
        total += together
    print(total)
    

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
