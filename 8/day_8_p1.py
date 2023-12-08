import sys
from typing import List

from dataclasses import dataclass



@dataclass
class Node:
    name : str
    left : 'Node'
    right : 'Node'


nodes : List[Node] = []

def get_node(name : str):
    for node in nodes:
        if node.name == name:
            return node
    node = Node(name, None, None)
    nodes.append(node)
    return node


def move(node , dir):
    counter = 0
    ind = 0
    while(node.name != 'ZZZ'):
        node = node.left if dir[ind] == 'L' else node.right
        counter+=1
        ind = (ind + 1) % len(dir)
    return counter



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
    print(move(get_node('AAA'), pattern.strip()))




if __name__ == '__main__':
    main(sys.argv, len(sys.argv))
