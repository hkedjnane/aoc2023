from functools import lru_cache
import sys
import itertools
import multiprocessing
import re

from dataclasses import dataclass

@dataclass
class Placeholder:
    x : int
    y : str


#=============================================
# TYPES

# Type of atomic input element
raw_input_t = list[str]
line_t = (list[int], list[list[int]])
input_t = list[line_t]

OP = 0
DMG = 1
NA = -1

stoi = {
    '.' : OP,
    '#' : DMG,
    '?' : NA
}

#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return list(filter(None, [line.strip() for line in open(file).readlines()]))


# treats a single line of the input
def treat_line(line : str) -> line_t:
    springs, consecutive = line.split(' ')
    springs = re.sub('\.+', '.', springs)
    print(springs)
    springs = [stoi[x] for x in springs] 
    consecutive = [int(x) for x in consecutive.split(',')]
    return springs, consecutive





# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t, level = 1) -> input_t:
    treated : input_t = []
    for line in input:
        treated.append(treat_line(line))
    return treated



#==============================================
# SOLUTION PART 1


    





@lru_cache
def rec(line : line_t):
    springs, cons = line
    def dmg():
        con = cons[0]
        if len(springs) < con:
            return 0
        damaged = [DMG if x  == NA else x for x in springs[:con]]
        cmp = [DMG] * con
        if damaged != cmp:
            return 0
        
        if len(springs) == con:
            return 1 if len(cons) == 1 else 0

        if springs[con] == DMG:
            return 0
        return rec((springs[con+1:],cons[1:]))
        
    def op():
        return rec((springs[1:],cons))


    if len(springs) == 0:
        return 1 if len(cons) == 0 else 0
    if len(cons) == 0:
        return 1 if DMG not in springs else 0

    c = springs[0]
    v1 = op() if c != DMG else 0
    v2 = dmg() if c != OP else 0
    return v1 + v2
    




def get_count(line : line_t):


    springs, cons = line
    return rec((tuple(springs), tuple(cons)))



def solve(data : input_t) -> int:
    pool = multiprocessing.Pool(8)
    s = pool.map(get_count, data)
    return sum(s)
    


#================================================
# SOLUTION PART 2

def solve2(data : input_t) -> int:
    for i, line in enumerate(data):
        springs, consecutive = line
        springs.append(NA)
        springs *=5
        springs = springs[:-1]
        consecutive *= 5
        data[i] = (springs, consecutive)
    return solve(data)

#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
