import sys
from copy import deepcopy

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

def inf(a, b):
    return a < b

def sup(a, b):
    return a > b

def inf_range(r, b):
    minimum, maximum = r
    included = None if b <= minimum else minimum, min(maximum, b - 1)
    excluded = None if b > maximum else b, maximum

    return included, excluded

def sup_range(r, b):
    minimum, maximum = r
    included = None if b >= maximum else max(minimum, b + 1), maximum
    excluded = None if b < minimum else minimum, b

    return included, excluded


mtof = {
    '<' : inf,
    '>' : sup
}

mtor = {
    '<' : inf_range,
    '>' : sup_range
}

# gets the input from the file and does minimum cleanup
def get_input(file : str) -> raw_input_t:
    return open(file).read().split('\n\n')


def treat_flow(flow : str, d = dict):
    first_bracket = flow.find('{')
    name = flow[:first_bracket]
    conditions = flow[first_bracket + 1:-1].split(',')
    default = conditions[-1]
    conditions = conditions[:-1]
    conds = []
    for cond in conditions:
        var = cond[0]
        check = cond[1]
        colon = cond.find(':')
        num_cmp = int(cond[2:colon])
        next_flow = cond[colon+1:]
        conds.append((var, check, num_cmp, next_flow))
    d[name] = (conds, default)

def treat_part(part):
    args = part[1:-1].split(',')
    part = {}
    for arg in args:
        arg = arg.strip().split('=')
        part[arg[0]] = int(arg[1])
    return part


# input is already separated by lines
# returns treatment for each line
def treat_input(input : raw_input_t) -> input_t:
    flows_str, parts_str = input
    parts = []
    flows = {}
    for flow in filter(None,flows_str.split('\n')):
        treat_flow(flow.strip(), flows)
    for part in filter(None,parts_str.split('\n')):
        parts.append(treat_part(part.strip()))
    return (flows, parts)



#==============================================
# SOLUTION PART 1

def valid_part(flows, part):
    flow = "in"
    while flow != "A" and flow != "R":
        conds, next = flows[flow]
        for cond in conds:
            var, check, num, next_flow = cond
            if mtof[check](part[var], num):
                next = next_flow
                break
        flow = next
    return flow == "A"


def solve(data : input_t) -> int:
    flows, parts = data
    total = 0
    for part in parts:
        if valid_part(flows, part):
            for value in part.values():
                total += value
    return total
    

        
#================================================
# SOLUTION PART 2

def constrain_part(flows, part, flow = "in"):
    #print(part)
    if flow == 'A':
        total = 1
        for r in part.values():
            total *= r[1] - r[0] + 1
        return total
    if flow == 'R':
        return 0
    
    total = 0
    
    checks, default = flows[flow]
    for var, check, num, next_flow in checks:
        included, excluded = mtor[check](part[var], num)
        if included != None:
            cp = deepcopy(part)
            cp[var] = included
            total += constrain_part(flows, cp, next_flow)
        if excluded == None:
            return total
        part[var] = excluded
    total += constrain_part(flows, part, default)
    return total




def solve2(data : input_t) -> int:
    flows, _ = data
    part = {'x' : (1, 4000), 'm' : (1, 4000), 'a' : (1, 4000), 's' : (1, 4000)}
    return constrain_part(flows, part)



#================================================


def main(argv, argc):
    input = get_input(argv[1])
    treated = treat_input(input)
    treated2 = deepcopy(treated)
    print("Solution 1: ", solve(treated))
    print("Solution 2: ", solve2(treated2))






if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
    
#def bruh(a : int):
#    print(a[1:-1])

#bruh("hello world")
