
import math
import sys
from typing import List

from dataclasses import dataclass



@dataclass
class Node:
    name : str
    left : 'Node'
    right : 'Node'
    end : bool


nodes : List[Node] = []
starts : List[Node] = []

def get_node(name : str):
    for node in nodes:
        if node.name == name:
            return node
    node = Node(name, None, None, name.endswith('Z'))
    nodes.append(node)
    if (name.endswith('A')):
        starts.append(node)
    return node




def move_one(node : Node, dir):
    counter = 0
    ind = 0
    while not node.name.endswith('Z'):
        node = node.left if dir[ind] == 'L' else node.right
        counter+=1
        ind = (ind + 1) % len(dir)
    return counter

def move(node_starts , dir):
    steps_to = []
    for node in node_starts:
        steps_to.append(move_one(node, dir))
    lcm = 1
    for i in steps_to:
        lcm = lcm*i//math.gcd(lcm, i)
    return lcm

    








def build_graph(lines : str):
    for line in filter(None,lines.split('\n')):
        parent, children = line.split('=')
        parent = get_node(parent.strip())
        left, right = children.replace('(', '').replace(')', '').strip().split(', ')
        parent.left = get_node(left.strip())
        parent.right = get_node(right.strip())





def main(argv, argc):
    pattern, nodes_str = open(argv[1]).read().split('\n\n')
    build_graph(nodes_str)
    #print('digraph {')
    #for graph in nodes:
    #    print(f'   {graph.name} -> {graph.left.name};')
    #    print(f'   {graph.name} -> {graph.right.name};')
    #print('}')
    print(move(starts, pattern.strip()))




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
