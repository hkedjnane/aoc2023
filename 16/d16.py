import sys

from dataclasses import dataclass
sys.setrecursionlimit(1000000000)

@dataclass
class Placeholder:
    x : int
    y : str

EMPTY = 0
MIRROR = 1
BMIRROR = 2
VSPLITTER = 3
HSPLITTER = 4
LIT = 5

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

m = {
    '.' : EMPTY,
    '/' : MIRROR,
    '\\': BMIRROR,
    '|' : VSPLITTER,
    '-' : HSPLITTER,
    '#' : LIT
}

dtm = {
    UP : (-1, 0),
    DOWN : (1, 0),
    LEFT : (0, -1),
    RIGHT : (0, 1)
}

mirror_change = [RIGHT, LEFT, DOWN, UP]
bmirror_change = [LEFT, RIGHT, UP, DOWN]


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
    values = [m[x] for x in line]
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

def add_tuple(t1, t2):
    return tuple(sum(t) for t in zip(t1, t2))

def print_maze(maze):
    for line in maze:
        for c in line:
            print('#' if True in c else '.', end="")
        print()

def solve(data : input_t, initial_coords = (0, 0), initial_direction = RIGHT) -> int:

    d1, d2 = len(data), len(data[0])

    lit = [[[False for _ in range(4)] for _ in range(d2)] for _ in range(d1)]
    #print(lit)

    def direct_light(coords, direction):
        x, y = coords

        d = lit[x][y]
        if d[direction]:
            return
        lit[x][y][direction] = True

        at = data[x][y]
        if at == EMPTY:
            return move_laser(coords, direction)
        if at == MIRROR:
            new_dir = mirror_change[direction]
            return move_laser(coords, new_dir)
        if at == BMIRROR:
            new_dir = bmirror_change[direction]
            return move_laser(coords, new_dir)
        if at == VSPLITTER:
            if direction == DOWN or direction == UP:
                return move_laser(coords, direction)
            move_laser(coords, UP)
            return move_laser(coords, DOWN)
        if at == HSPLITTER:
            if direction == LEFT or direction == RIGHT:
                return move_laser(coords, direction)
            move_laser(coords, LEFT)
            return move_laser(coords, RIGHT)
            
    def move_laser(coords, direction):
        #print(coords, direction)
        x, y = add_tuple(coords, dtm[direction])
        if x < 0 or x >= d1 or y < 0 or y >= d2:
            return 0
        return direct_light((x, y), direction)
    
    def count_lit():
        total = 0
        for line in lit:
            for c in line:
                if True in c:
                    total+=1
        return total

    
    direct_light(initial_coords, initial_direction)
    #print_maze(lit)
    
    return count_lit()




#================================================
# SOLUTION PART 2

def solve2(data : input_t) -> int:
    m = 0
    d1, d2 = len(data), len(data[0])
    for i in range(d2):
        m = max(m, solve(data, (0, i), DOWN))
        m = max(m, solve(data, (d1 - 1, i), UP))
    for i in range(d1):
        m = max(m, solve(data, (i, 0), RIGHT))
        m = max(m, solve(data, (i, d2 - 1), LEFT))
    return m




#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
