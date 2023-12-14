from functools import lru_cache
import sys

from dataclasses import dataclass

@dataclass
class Placeholder:
    x : int
    y : str

GROUND = 0
ROUND = 1
FIXED = 2

m = {
    '.' : GROUND,
    'O' : ROUND,
    '#' : FIXED
}

#=============================================
# TYPES

# Type of atomic input element
raw_input_t = list[str]
input_t = list[list[int]]
line_t = list[int]


#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return list(filter(None, [line.strip() for line in open(file).readlines()]))


# treats a single line of the input
def treat_line(line : str) -> line_t:
    values = [m[x] for x in list(line)]
    return values

# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    treated = []
    for line in input:
        treated.append(treat_line(line))
    return treated


#==============================================
# SOLUTION PART 1

def print_rocks(rocks : input_t):
    for line in rocks:
        for c in line:
            if c == GROUND:
                print('.', end="")
            elif c == ROUND:
                print('O', end="")
            else:
                print('#', end="")
        print()

def get_load(rocks : input_t):
    total = 0
    highest = [0] * len(rocks)
    for y in range(len(rocks[0])):
        for x in range(len(rocks)):
            c = rocks[x][y]
            if c == FIXED:
                highest[y] = x + 1
            elif c == ROUND:
                rocks[x][y] = GROUND
                rocks[highest[y]][y] = ROUND
                highest[y] = highest[y] + 1
                total += len(rocks) - highest[y] + 1
    return total


def solve(data : input_t) -> int:
    return get_load(data)


#================================================
# SOLUTION PART 2

north = {

}

south = {

}

east = {

}

west = {

}

def get_key(rocks, it, dict : dict):
    fixed = []
    round = []
    for x, line in enumerate(rocks):
        for y, c in enumerate(line):
            if c == ROUND:
                round.append(x * len(rocks[0]) + y)
            elif c == FIXED:
                fixed.append(x * len(rocks[0]) + y)
    key = (tuple(fixed), tuple(round))
    v = dict.get(key, -1)
    dict[key] = it
    return v
            
def rotate(matrix):
    transposed = []
    for row in zip(*matrix):
        transposed.append(list(row))
    rotated = []
    for row in transposed:
        rotated.append(row[::-1])
    return rotated

def rotate_counter(m):
    return list(map(list, zip(*m)))[::-1]



def move(rocks : input_t):
    highest = [0] * len(rocks)
    for y in range(len(rocks[0])):
        for x in range(len(rocks)):
            c = rocks[x][y]
            if c == FIXED:
                highest[y] = x + 1
            elif c == ROUND:
                rocks[x][y] = GROUND
                rocks[highest[y]][y] = ROUND
                highest[y] = highest[y] + 1
    return rocks

def move_south(rocks : input_t):
    rocks.reverse()
    rocks = move(rocks)
    rocks.reverse()
    return rocks

def move_north(rocks : input_t):
    return move(rocks)

def move_west(rocks):
    rocks = rotate(rocks)
    rocks = move(rocks)
    rocks = rotate_counter(rocks)
    return rocks

def move_east(rocks):
    rocks = rotate_counter(rocks)
    rocks = move(rocks)
    rocks = rotate(rocks)
    return rocks


def move_dir(rocks, it):
    callbacks = [move_north, move_west, move_south, move_east]
    d = [north, west, south, east]
    rocks = callbacks[it % len(callbacks)](rocks)
    return rocks, get_key(rocks, it, d[it % len(d)])


def get_load2(rocks : input_t):
    total = 0
    for x in range(len(rocks)):
        for y in range(len(rocks)):
            c = rocks[x][y]
            if c == ROUND:
                total += len(rocks) - x
    return total



def solve2(data : input_t) -> int:
    i = 0
    turns = 1000000000 * 4
    while i < turns:
        #print(i)
        data, last = move_dir(data, i)
        #print_rocks(data)
        if last == -1:
            i+=1
            continue
        gap = i - last
        remaining = turns - i
        gap_nb = int(remaining/gap)
        i += gap_nb * gap + 1
    return get_load2(data)



#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
