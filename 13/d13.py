import sys

from dataclasses import dataclass

@dataclass
class Placeholder:
    x : int
    y : str

G = 0
M = 1

m = {
    '.' : G,
    '#' : M
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
    return list(filter(None, [line.strip() for line in open(file).read().split('\n\n')]))


# treats a single line of the input
def treat_matrix(matrix : str) -> line_t:
    mat = []
    lines = matrix.split('\n')
    for line in lines:
        l = []
        for c in line:
            l.append(m[c])
        mat.append(l)
    return mat

# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    treated = []
    for line in input:
        treated.append(treat_matrix(line))
    return treated


#==============================================
# SOLUTION PART 1


def find_horizontal(mat, mult = 100):

    def check_center(center):
        d1, d2 = len(mat), len(mat[0])
        for i in range(1,min(center + 1, d1 - center - 1)):
            l1, l2 = mat[center - i], mat[center + i + 1]
            for i in range(d2):
                if l1[i] != l2[i]:
                    return False
        return True

    d1, d2 = len(mat), len(mat[0])
    for i in range(d1 - 1):
        l1, l2 = mat[i],mat[i+1]
        center = True
        for j in range(d2):
            if l1[j] != l2[j]:
                center = False
                break
        if center and check_center(i):
            return (i + 1) * mult
    return -1


    



def rotated(mat):
    return [list(reversed(col)) for col in zip(*mat)]

def get_count(mat):
    v1 = find_horizontal(mat)
    return v1 if v1 != -1 else find_horizontal(rotated(mat), 1)



def solve(data : input_t) -> int:
    total = 0
    for mat in data:
        total += get_count(mat)
    return total

#================================================
# SOLUTION PART 2

def find_smudge(mat, mult = 100):

    def check_center(center, smudge):
        d1, d2 = len(mat), len(mat[0])
        for i in range(1,min(center + 1, d1 - center - 1)):
            l1, l2 = mat[center - i], mat[center + i + 1]
            for i in range(d2):
                if l1[i] != l2[i]:
                    if not smudge:
                        smudge = True
                    else:
                        return False
        return smudge

    d1, d2 = len(mat), len(mat[0])
    for i in range(d1 - 1):
        smudge = False
        l1, l2 = mat[i],mat[i+1]
        center = True
        for j in range(d2):
            if l1[j] != l2[j]:
                if not smudge:
                    smudge = True
                else:
                    center = False
                    break
        if center and check_center(i, smudge):
            return (i + 1) * mult
    return -1




def get_count2(mat):
    v1 = find_smudge(mat)
    return v1 if v1 != -1 else find_smudge(rotated(mat), 1)

def solve2(data : input_t) -> int:
    total = 0
    for mat in data:
        total += get_count2(mat)
    return total


#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
