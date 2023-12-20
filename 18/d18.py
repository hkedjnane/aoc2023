import math
import sys
sys.setrecursionlimit(100000000)
from dataclasses import dataclass
from copy import deepcopy

@dataclass
class Placeholder:
    x : int
    y : str

R = 0
D = 1
L = 2
U = 3

vect = [(0, 1), (1, 0), (0, -1), (-1, 0)]


EMPTY = 0
DUG = 1
OUTSIDE = 2
INSIDE = 3


m = {
    'U' : U,
    'D' : D,
    'L' : L,
    'R' : R
}

#=============================================
# TYPES

# Type of atomic input element
raw_input_t = list[str]
line_t = (int, int, str)
input_t = list[line_t]


#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return list(filter(None, [line.strip() for line in open(file).readlines()]))


# treats a single line of the input
def treat_line(line : str) -> line_t:
    dir, count, color   = [x.strip() for x in line.split(' ')]
    return m[dir], int(count), color[2:-1]

# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    treated = []
    for line in input:
        treated.append(treat_line(line))
    return treated


#==============================================
# SOLUTION PART 1


def print_dug(repr):
    for line in repr:
        for c in line:
            print('.' if c == EMPTY or c == OUTSIDE else '#', end="")
        print()

def add_tuple(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])

def mult_tuple(t, n):
    return t[0] * n, t[1] * n

def spread_count(repr, x, y):
    repr[x][y] = DUG
    total = 1
    outside = False
    d1, d2 = len(repr), len(repr[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i,j) == (0, 0):
                continue
            x2, y2 = x + i, y + j
            if x2 < 0 or x2 >= d1 or y2 < 0 or y2 >= d2:
                outside = True
                continue
            c = repr[x2][y2]
            if c != EMPTY:
                continue
            part, is_inside = spread_count(repr, x2, y2)
            if not is_inside:
                outside = True
            else:
                total += part
    if outside:
        repr[x][y] = OUTSIDE
        return 0, False
    return total, True
            


def count_inside(repr):
    total = 0
    for x, line in enumerate(repr):
        for y, c in enumerate(line):
            if c == EMPTY:
                part, _ = spread_count(repr, x, y)
                total += part
    return total





def solve(data : input_t) -> int:
    min_h, max_h, min_v, max_v, curr_h, curr_v = 0, 0, 0, 0, 0,0
    for dir, count, _ in data:
        if dir == R or dir == L:
            curr_h += count * (1 if dir == R else -1)
            if curr_h < min_h:
                min_h = curr_h
            if curr_h > max_h:
                max_h = curr_h
        elif dir == U or dir == D:
            curr_v += count * (1 if dir == D else -1)
            if curr_v < min_v:
                min_v = curr_v
            if curr_v > max_v:
                max_v = curr_v
    repr = [[EMPTY for _ in range(max_h - min_h + 1)] for _ in range(max_v - min_v + 1)]
    x, y = (abs(min_v), abs(min_h))
    repr[x][y] = DUG
    total = 0
    for dir, count, _ in data:
        for _ in range(count):
            x, y = add_tuple((x, y), vect[dir])
            repr[x][y] = DUG
            total += 1
    print_dug(repr)
    total += count_inside(repr)
    return total









#================================================
# SOLUTION PART 2

def convert_input(data):
    d = []
    for line in data:
        _, _, color = line
        count = int(color[:5], 16)
        dir = int(color[-1])
        d.append((dir, count))
    return d


def get_point_list(data):
    origin = (0,0)
    points = [origin]
    total = 0
    for dir, count in data:
        origin = add_tuple(origin, mult_tuple(vect[dir], count))
        points.append(origin)
        total += count
    return points[:-1], int(total/2 + 1)

def shoelace(vertices):
    #A function to apply the Shoelace algorithm
    numberOfVertices = len(vertices)
    sum1 = 0
    sum2 = 0

    for i in range(0,numberOfVertices-1):
      sum1 = sum1 + vertices[i][0] *  vertices[i+1][1]
      sum2 = sum2 + vertices[i][1] *  vertices[i+1][0]

    #Add xn.y1
    sum1 = sum1 + vertices[numberOfVertices-1][0]*vertices[0][1]   
    #Add x1.yn
    sum2 = sum2 + vertices[0][0]*vertices[numberOfVertices-1][1]   

    area = abs(sum1 - sum2) / 2
    return area



def solve2(data : input_t):
    data = convert_input(data)
    data, total = get_point_list(data)
    print(data)
    return total + int(shoelace(data))



#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = deepcopy(treated)
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
