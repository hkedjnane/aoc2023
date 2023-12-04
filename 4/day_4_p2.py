import sys

def main(argv, argc):
    total = 0
    input = argv[1]
    curr_game = 0
    game_copies = [[line, 1] for line in open(input).readlines()]
    for line, copies in game_copies:
        line = line.split(':')[1].strip()
        actual, winning = line.split('|')
        actual = [int(s) for s in filter(None,actual.strip().split(' '))]
        winning = [int(s) for s in filter(None,winning.strip().split(' '))]
        matching = 0
        for num in actual:
            if num in winning:
                matching+=1
        for i in range(matching):
            game_copies[curr_game+i + 1][1] += copies
        curr_game+=1
    total = 0
    print(game_copies)
    for _, copies in game_copies:
        total += copies
    print(total)
    


if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
