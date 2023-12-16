import sys

from dataclasses import dataclass

@dataclass
class Placeholder:
    x : int
    y : str


#=============================================
# TYPES

# Type of atomic input element
raw_input_t = str
input_t = list[str]
line_t = str


#=============================================
# INPUT TREATMENT

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return open(file).read()


# treats a single line of the input
#def treat_line(line : str) -> line_t:
#    values = [int(x.strip()) for x in line.split(' ')]
#    return values

# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    return [x.strip() for x in input.split(',')]


#==============================================
# SOLUTION PART 1


def ascii_solve(line : line_t) -> int:
    value = 0
    for c in line:
        value += ord(c)
        value *= 17
        value %= 256
    print(line, value)
    return value

def solve(data : input_t) -> int:
    total = 0
    for line in data:
        total += ascii_solve(line)
    return total


#================================================
# SOLUTION PART 2


def print_lenses(lenses):
    for i, d in enumerate(lenses):
        if d == {}:
            continue
        print(i, d)

def minus_op(lens, lenses : list[dict[str, int]]):
    key = lens[:-1]
    lenses[ascii_solve(key)].pop(key, 0)

def equals_op(lens, lenses : list[dict[str, int]], eq_index):
    key, value = lens.split('=')
    value = int(value)
    lenses[ascii_solve(key)][key] = value



def lens_logic(lens : line_t,lenses):
    has_equal = lens.find('=')
    if has_equal != -1:
        return equals_op(lens, lenses, has_equal)
    return minus_op(lens, lenses)


def get_total(lenses : list[dict[str, int]]):
    total = 0
    for box, d in enumerate(lenses):
        for slot, p in enumerate(d.values()):
            total += (box + 1) * (slot + 1) * p
    return total


def solve2(data : input_t) -> int:
    lenses = [{} for _ in range(256)]
    for lens in data:
        lens_logic(lens, lenses)
    return get_total(lenses)


#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
