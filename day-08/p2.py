from itertools import cycle
from math import lcm
from importlib import import_module

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    movements, instructions = import_module('1').parse_input(lines)
        
    start_nodes = [instructions.get(node) for node in instructions if node[-1] == 'A']
    end_nodes = [instructions.get(node) for node in instructions if node[-1] == 'Z']

    total_moves = []

    for start_node in start_nodes:
        current_node = start_node
        current_moves = 0

        while current_node not in end_nodes:
            current_node = instructions.get(current_node[next(movements)])
            current_moves += 1
                
        total_moves.append(current_moves)
    
    return lcm(*total_moves)

if __name__ == "__main__":
    print(main())