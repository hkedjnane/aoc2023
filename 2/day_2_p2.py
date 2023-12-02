import sys

rgb_index = {
    'red' : 0,
    'green' : 1,
    'blue' : 2
}

def minimum_game_power(game : str) -> int:
    max_rgb = [0, 0, 0]
    # strip the  "Game n:" component
    game = game[game.find(':')+1::].strip()
    # split along ';' delimiter
    handfuls = game.split(';')
    for handful in handfuls:
        #split along ',' to get handful rgb
        handful_rgb = handful.strip().split(',')
        print(handful_rgb)
        for color_handful in handful_rgb:
            #split along the space between the number and the color
            color_handful = color_handful.strip().split(' ')
            print(color_handful)
            color_number = int(color_handful[0])
            color_index = rgb_index[color_handful[1]]
            max_rgb[color_index] = max(max_rgb[color_index], color_number)
    return max_rgb[0] * max_rgb[1] * max_rgb[2]


def main(argv, argc):
    total = 0
    for game in open(argv[1]).readlines():
        total += minimum_game_power(game)
    print(total)
    

if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
