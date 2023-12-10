import sys

sys.setrecursionlimit(1000000)

from dataclasses import dataclass

@dataclass
class C:
    x : int
    y : int

direction = {
    '.' : [C(0,0),C(0,0)],
    '|' : [C(1,0),C(-1,0)],
    'J' : [C(0, -1),C(-1, 0)],
    'L' : [C(0,1),C(-1, 0)],
    '7' : [C(1,0),C(0, -1)],
    'F' : [C(1,0),C(0, 1)],
    'S' : [C(0,0),C(0,0)],
    '-' : [C(0,1), C(0, -1)]
}

come_from = {
    '.' : [C(0,0), C(0,0)],
    '|' : [C(1,0),C(-1,0)],
    'J' : [C(1, 0),C(0, 1)],
    'L' : [C(1,0),C(0, -1)],
    '7' : [C(0,1),C(-1, 0)],
    'F' : [C(0,-1), C(-1, 0)],
    'S' : [C(0,0),C(0,0)],
    '-' : [C(0, 1), C(0, -1)]
}


double_left = {
    ',' : ',',
    '.' : ',',
    '|' : ',',
    'J' : ',',
    'L' : '-',
    '7' : ',',
    'F' : '-',
    '-' : '-',
}


double_down = {
    ',' : ',',
    '.' : ',',
    '|' : '|',
    'J' : ',',
    'L' : ',',
    '7' : '|',
    'F' : '|',
    '-' : ',',
}

s_coords : C = None
d1 = None
d2 = None

#=============================================
# TYPES

# Type of atomic input element
raw_input_t = list[str]
input_t = list[list[str]]
line_t = list[str]


#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return list(filter(None, [line.strip() for line in open(file).readlines()]))


# treats a single line of the input
def treat_line(line : str, ind : int) -> line_t:
    global s_coords
    x = []
    for i, c in enumerate(line):
        x.append(c)
        if c == 'S':
            s_coords = C(ind, i)
    return x

# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    treated = []
    for i, line in enumerate(input):
        treated.append(treat_line(line, i))
    return treated

def add(a : C, b : C):
    return C(a.x + b.x, a.y + b.y)

def cmp(a : C, b : C):
    return a.x == b.x and a.y == b.y


#==============================================
# SOLUTION PART 1


def find_connections(maze : input_t, c : (int, int), dir_int : int):
    pipe = maze[c.x][c.y]
    dir = direction[pipe][dir_int]
    next = add(c, dir)
    if next.x < 0 or next.x >= d1 or next.y < 0 or next.y >= d2:
        return None, -1 
    frm = come_from[maze[next.x][next.y]]
    if cmp(dir, frm[0]):
        return next, 0
    if cmp(dir, frm[1]):
        return next, 1
    return None, -1


#find the pipe for which the starting pipe has two connection, one for each exit
def find_starting_pipe(maze : input_t):
    global s_coords, d1, d2
    for pipe in direction.keys():
        if (pipe == 'S' or pipe == '.'):
            continue
        maze[s_coords.x][s_coords.y] = pipe
        coords1, dir1 = find_connections(maze, s_coords, 0)
        if (coords1 == None):
            continue
        coords2, dir2 = find_connections(maze, s_coords, 1)
        if (coords2 == None):
            continue
        return [(coords1, dir1), (coords2, dir2)]





def solve(data : input_t) -> int:
    maze = data
    global s_coords
    (c1, dir1), (c2, dir2) = find_starting_pipe(maze)
    distance = 1
    while not cmp(c1, c2):
        c1, dir1 = find_connections(maze, c1, dir1)
        c2, dir2 = find_connections(maze, c2, dir2)
        distance+=1
    return distance



#================================================
# SOLUTION PART 2

def double_map(maze : input_t):
    doubled = []
    for line in maze:
        doubled_left = []
        doubled_down = []
        for c in line:
            c_left = double_left[c]
            c_down = double_down[c]
            c_left_down = double_down[c_left]
            doubled_left.append(c)
            doubled_left.append(c_left)
            doubled_down.append(c_down)
            doubled_down.append(c_left_down)
        doubled.append(doubled_left)
        doubled.append(doubled_down)
    return doubled

def get_empty(maze, x, y, count, outside = False):
    maze[x][y] = 'I'
    r = [-1, 0, 1]
    for i in r:
        for j in r:
            if (i, j) == (0, 0):
                continue
            x2, y2 = x+i, y + j
            if x2 < 0 or y2 < 0 or x2 >= d1 or y2 >= d2:
                outside = True
                continue
            c = maze[x2][y2]
            if (c != '.' and c != ','):
                continue
            count, outside = get_empty(maze, x2, y2, count + 1 if c == '.' else count, outside)
    if outside:
        maze[x][y] = 'O'
    return count, outside




def print_map(maze):
    for line in maze:
        for c in line: 
            print(c, end = '')
        print()
    print()
    print()
    print()



def solve2(data : input_t) -> int:
    global s_coords, d1, d2
    maze = data
    (c1, dir1), (c2, dir2) = find_starting_pipe(maze)
    distance = 1
    maze_clean = []
    for i in range(d1):
        bruh = []
        for i in range(d2):
            bruh.append('.')
        maze_clean.append(bruh)
    maze_clean[s_coords.x][s_coords.y] = maze[s_coords.x][s_coords.y]
    maze_clean[c1.x][c1.y] = maze[c1.x][c1.y]
    maze_clean[c2.x][c2.y] = maze[c2.x][c2.y]
    while not cmp(c1, c2):
        c1, dir1 = find_connections(maze, c1, dir1)
        c2, dir2 = find_connections(maze, c2, dir2)
        maze_clean[c1.x][c1.y] = maze[c1.x][c1.y]
        maze_clean[c2.x][c2.y] = maze[c2.x][c2.y]
        distance+=1
    doubled = double_map(maze_clean)
    d1 = len(doubled)
    d2 = len(doubled[0])
    total = 0
    for x in range(d1):
        for y in range(d2):
            c = doubled[x][y]
            if c != '.' and c != ',':
                continue
            count, outside = get_empty(doubled, x, y, 1 if c == '.' else 0)
            if not outside:
                total += count
    return total
    



#================================================


def main(argv, argc):
    global d1, d2
    input = get_input(argv[1])
    treated = treat_input(input)
    d1 = len(treated)
    d2 = len(treated[0])
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
