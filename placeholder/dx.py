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




def solve(data : input_t) -> int:
    pass
#================================================
# SOLUTION PART 2

def solve2(data : input_t) -> int:
    pass


#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
