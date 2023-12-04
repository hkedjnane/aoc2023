import sys

def main(argv, argc):
    total = 0
    input = argv[1]
    for line in open(input).readlines():
        points = 0
        line = line.split(':')[1].strip()
        actual, winning = line.split('|')
        print(actual)
        print(winning)
        actual = [int(s) for s in filter(None,actual.strip().split(' '))]
        winning = [int(s) for s in filter(None,winning.strip().split(' '))]
        for num in actual:
            if num in winning:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        total += points

    print(total)


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
