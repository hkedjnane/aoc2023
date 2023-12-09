import sys

from dataclasses import dataclass

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
    values = [int(x.strip()) for x in line.split(' ')]
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



#return the interval list of the current iteration as well as a boolean indicating the list is only zeroes
def get_intervals(incr : line_t) -> (int, bool):
    intervals = []
    is_zeroes = True
    for i in range(len(incr) - 1):
        v1 = incr[i]
        v2 = incr[i+1]
        diff = v2 - v1
        if (diff != 0):
            is_zeroes = False
        intervals.append(v2-v1)
    if is_zeroes:
        intervals.append(0)
    return intervals, is_zeroes


def extrapolate(incr : line_t) -> int:
    iterations = []
    iterations.append(incr)
    while True:
        incr, done = get_intervals(incr)
        iterations.append(incr)
        if done:
            break
    for i in reversed(range(1, len(iterations))):
        last = iterations[i]
        prev = iterations[i-1]
        prev.append(last[-1] + prev[-1])
    return iterations[0][-1]



def solve(data : input_t) -> int:
    solution : int = 0
    for line in data:
        solution += extrapolate(line)
    return solution



#================================================
# SOLUTION PART 2

def rev_extrapolate(incr : line_t) -> int:
    iterations : list[list[int]] = []
    iterations.append(incr)
    while True:
        incr, done = get_intervals(incr)
        iterations.append(incr)
        if done:
            break
    for i in reversed(range(1, len(iterations))):
        last = iterations[i]
        prev = iterations[i-1]
        prev.insert(0, prev[0] - last[0])
    return iterations[0][0]


def solve2(data : input_t) -> int:
    solution : int = 0
    for line in data:
        solution += rev_extrapolate(line)
    return solution


#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
