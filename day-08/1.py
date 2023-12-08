from itertools import cycle
from typing import Tuple, Iterator

def parse_input(lines: list) -> Tuple[Iterator, dict]:
    movements = cycle(lines[0].strip())

    instructions = {
        key.strip(): {
            'L': ''.join(filter(str.isalnum, value.split(',')[0])),
            'R': ''.join(filter(str.isalnum, value.split(',')[1])),
            'ID': key.strip()
        }
        for node in lines[2:]
        for key, value in [node.split('=')]
    }

    return movements, instructions

def main():
    with open("input.txt") as f:
        lines = f.readlines()
    
    movements, instructions = parse_input(lines)

    total_moves = 0
    current = instructions.get('AAA')
    end = instructions.get('ZZZ')

    while current != end:
        next_move = next(movements)
        total_moves += 1

        current = instructions.get(current[next_move])

    return total_moves

if __name__ == "__main__":
    print(main())