import sys

from dataclasses import dataclass
from collections import defaultdict
from functools import lru_cache
from copy import deepcopy

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


#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return list(filter(None, [line.strip() for line in open(file).readlines()]))


# treats a single line of the input
def treat_line(line : str) -> line_t:
    b1, b2 = line.split('~')
    x1, y1, z1 = b1.split(',')
    x2, y2, z2 = b2.split(',')
    return ((int(x1), int(y1), int(z1)),(int(x2), int(y2), int(z2)))


# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    treated = []
    for line in input:
        treated.append(treat_line(line))
    return treated


#==============================================
# SOLUTION PART 1


def sign(v):
    return 1 if v > 0 else -1 if v < 0 else 0

def add_tuple(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])

def mult_tuple(c, n):
    return (c[0] * n, c[1] * n, c[2] * n)



def solve(data : input_t) -> int:
    carrying = defaultdict(set)
    carried_by = defaultdict(set)
    z_at = defaultdict(lambda:(0, None))
    data = sorted(data, key=lambda x: x[0][2])



    def find_below(x, y):
        ground, below = z_at[(x,y)]
        return ground + 1, below
    
    def handle_brick(brick, index):
        coords1, coords2 = brick
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        if z2 != z1:
            ground, below = find_below(x1, y1)
            if below != None:
                carried_by[index].add(below)
                carrying[below].add(index)
            z_at[(x1, y1)] = (ground + abs(z2-z1), index)
            return
        carries = []
        coords = coords1
        max_ground = 1
        diff = (sign(x2-x1), sign(y2-y1), sign(z2-z1))
        while True:
            x, y, _ = coords
            ground, below = find_below(x, y)
            if below != None:
                if ground > max_ground:
                    max_ground = ground
                    carries = [below]
                elif max_ground == ground:
                    carries.append(below)
            if coords == coords2:
                break
            coords = add_tuple(coords, diff)
        for carry in carries:
            carried_by[index].add(carry)
            carrying[carry].add(index)
        coords = coords1
        while True:
            x, y, _ = coords
            z_at[(x, y)] = (max_ground, index)
            if coords == coords2:
                break
            coords = add_tuple(coords, diff)
            
        

    def can_disintegrate(index):
        for brick in carrying[index]:
            if len(carried_by[brick]) == 1:
                return False
        return True

    for i, brick in enumerate(data):
        handle_brick(brick, i)

    total = 0
    for i in range(len(data)):
        if can_disintegrate(i):
            total +=1

    return total







# SOLUTION PART 2

def solve2(data : input_t) -> int:
    carrying = defaultdict(set)
    carried_by = defaultdict(set)
    z_at = defaultdict(lambda:(0, None))
    data = sorted(data, key=lambda x: x[0][2])



    def find_below(x, y):
        ground, below = z_at[(x,y)]
        return ground + 1, below
    
    def handle_brick(brick, index):
        coords1, coords2 = brick
        x1, y1, z1 = coords1
        x2, y2, z2 = coords2
        if z2 != z1:
            ground, below = find_below(x1, y1)
            if below != None:
                carried_by[index].add(below)
                carrying[below].add(index)
            z_at[(x1, y1)] = (ground + abs(z2-z1), index)
            return
        carries = []
        coords = coords1
        max_ground = 1
        diff = (sign(x2-x1), sign(y2-y1), sign(z2-z1))
        while True:
            x, y, _ = coords
            ground, below = find_below(x, y)
            if below != None:
                if ground > max_ground:
                    max_ground = ground
                    carries = [below]
                elif max_ground == ground:
                    carries.append(below)
            if coords == coords2:
                break
            coords = add_tuple(coords, diff)
        for carry in carries:
            carried_by[index].add(carry)
            carrying[carry].add(index)
        coords = coords1
        while True:
            x, y, _ = coords
            z_at[(x, y)] = (max_ground, index)
            if coords == coords2:
                break
            coords = add_tuple(coords, diff)

        
    def chain_reaction(index, fallen):
        next_fallen = set()
        for carry in carrying[index]:
            if carry in fallen:
                continue
            carried = carried_by[carry]
            if carried.union(fallen) == fallen:
                fallen.add(carry)
                next_fallen.add(carry)
        total  = len(next_fallen)
        for fall in next_fallen:
            total += chain_reaction(fall, fallen)
        return total





    for i, brick in enumerate(data):
        handle_brick(brick, i)

    total = 0
    for i in range(len(data)):
        total += chain_reaction(i, set([i]))
    return total



#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = deepcopy(treated)
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
