import sys

rgb_index = {
    'red' : 0,
    'green' : 1,
    'blue' : 2
}

def is_valid_game(game : str, rgb : list[int]) -> bool:
    # strip the  "Game n:" component
    game = game[game.find(':')+1::].strip()
    # split along ';' delimiter
    handfuls = game.split(';')
    for handful in handfuls:
        #split along ',' to get handful rgb
        handful_rgb = handful.strip().split(',')
        for color_handful in handful_rgb:
            #split along the space between the number and the color
            color_handful = color_handful.strip().split(' ')
            color_number = int(color_handful[0])
            color = color_handful[1]
            if rgb[rgb_index[color]] < color_number:
                return False
    return True


def main(argv, argc):
    r = int(argv[2])
    g = int(argv[3])
    b = int(argv[4])
    rgb = [r,g,b]
    total = 0
    gameid = 1
    for game in open(argv[1]).readlines():
        if (is_valid_game(game.strip(), rgb)):
            total += gameid
        gameid+=1
    print(total)
    

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
