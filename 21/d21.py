import sys

from dataclasses import dataclass
from functools import lru_cache
from collections import defaultdict
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np

@dataclass
class Placeholder:
    x : int
    y : str


#=============================================
# TYPES

# Type of atomic input element
raw_input_t = list[str]
input_t = list[list[int]]
line_t = list[int]

GARDEN = 0
ROCK = 1
VISITED = 2
STARTING = 3

m = {
    '.' : GARDEN,
    '#' : ROCK,
    'O' : VISITED,
    'S' : STARTING
}



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

def print_input(data):
    inv_map = {v: k for k, v in m.items()}
    for line in data:
        for c in line:
            print(inv_map[c], end="")
        print()


def find_start(data):
    for x, line in enumerate(data):
        for y, c in enumerate(line):
            if c == STARTING:
                return x,y

def solve(data : input_t) -> int:
    print_input(data)
    d1, d2 = len(data), len(data[0])
    steps = 64
    startx, starty = find_start(data)
    data[startx][starty] = GARDEN
    at_step = set([(startx, starty)])
    for _ in range(steps):
        at_step_new = set()
        for garden in at_step:
            gx, gy = garden
            around = [(gx - 1, gy), (gx + 1, gy), (gx, gy - 1), (gx, gy + 1)]
            for ggx, ggy in around:
                if ggx < 0 or ggx >= d1 or ggy < 0 or ggy >= d2:
                    continue
                if data[ggx][ggy] == GARDEN:
                    at_step_new.add((ggx, ggy))
        at_step = at_step_new
    
    return len(at_step)

#================================================
# SOLUTION PART 2

def dict_to_tuples(d):
        t = []
        for k, v in d.items():
            t.append((k, tuple(v)))
        return tuple(t)


def solve2(data : input_t) -> int:
    print_input(data)
    d1, d2 = len(data), len(data[0])
    startx, starty = find_start(data)
    data[startx][starty] = GARDEN

    def reachable(pos):
        total = 0
        for _, v in pos:
            total += len(v)
        return total

    @lru_cache
    def look_around(coords):
        gx, gy = coords
        around = [(gx - 1, gy), (gx + 1, gy), (gx, gy - 1), (gx, gy + 1)]
        gardens = set()
        for ggx, ggy in around:
            ggxr, ggyr = ggx % d1, ggy % d2
            if data[ggxr][ggyr] == GARDEN:
                gardens.add((ggx, ggy))
        return gardens
    
    @lru_cache()
    def get_new_pos(pos):
        new_pos = defaultdict(set)
        for k,v in pos:
            for gx, gy in look_around(k):
                superxd, superyd = (1 if gx >= d1 else (-1 if gx < 0 else 0)), (1 if gy >= d2 else (-1 if gy < 0 else 0))
                gx, gy = gx % d1, gy % d2
                for superx, supery in v:
                    new_pos[(gx, gy)].add((superx + superxd, supery + superyd))
        return dict_to_tuples(new_pos)


    pos = (((startx, starty),((0, 0),)),)
    reachables = []
    initial = 1000
    for _ in range(initial):
        pos = get_new_pos(pos)
        reach = reachable(pos)
        reachables.append(reach)

    xs = [x for x in range(len(reachables))]

    curve = np.polyfit(xs, reachables, deg=2)

    final = 26501365

    return int(np.polyval(curve, final))



#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = deepcopy(treated)
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
