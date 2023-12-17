import sys

from dataclasses import dataclass
from heapq import heappop, heappush

@dataclass
class Placeholder:
    x : int
    y : str

NORTH = 0
SOUTH = 1
EAST = 2
WEST = 3

dirs = [NORTH, SOUTH, EAST, WEST]
backwards = [SOUTH, NORTH, WEST, EAST]
vect = [(-1, 0), (1, 0), (0, 1), (0, -1)]

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
    values = [int(x) for x in line]
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
    x1, y1 = t1
    x2, y2 = t2
    return (x1 + x2, y1 + y2)

def mult_tuple(t, n):
    x, y = t
    return (x * n, y * n)


def djikstra(maze, start, end, inf = 1, sup = 3):
    d1, d2 = len(maze), len(maze[0])
    startx, starty = start
    endx, endy = end
    h = [(0, (startx, starty, -1))]
    checked = set()
    dist = {}
    dist[(startx, starty, -1)] = 0


    while len(h) != 0:
        distance, (x, y, curr_dir)  = heappop(h)

        if (x,y) == end:
            return distance

        if (x,y,curr_dir) in checked:
            continue

        checked.add((x,y,curr_dir))

        
        for dir in dirs:
            if curr_dir != -1 and (dir == curr_dir or dir == backwards[curr_dir]):
                continue
            new_dist = distance
            for i in range(1, sup + 1):
                new_x, new_y = add_tuple((x, y), mult_tuple(vect[dir], i))
                if new_x < 0 or new_x >= d1 or new_y < 0 or new_y >= d2:
                    break
                next_dist = dist.get((new_x, new_y, curr_dir), 1e7)
                new_dist += maze[new_x][new_y]
                if i < inf:
                    continue
                if new_dist < next_dist:
                    heappush(h,(new_dist, (new_x, new_y, dir)))
                    dist[(new_x, new_y, curr_dir)] = new_dist

    return dist[endx][endy]





def solve(data : input_t) -> int:
    d1, d2 = len(data), len(data[0])
    start = (0, 0)
    end = (d1 - 1, d2 - 1)
    return djikstra(data, start, end)
#================================================
# SOLUTION PART 2

def solve2(data : input_t) -> int:
    d1, d2 = len(data), len(data[0])
    start = (0, 0)
    end = (d1 - 1, d2 - 1)
    return djikstra(data, start, end, 4, 10)


#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = treated.copy()
    print("Solution 1: ", solve(treated2))
    print("Solution 2: ", solve2(treated))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
