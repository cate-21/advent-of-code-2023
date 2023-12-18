from typing import Tuple
from functools import cache

@cache
def count_arrangements(record: str, groups: Tuple[int,...]) -> int:

    if not groups:
        return 1 if '#' not in record else 0

    if (sum(groups) + len(groups) - 1) > len(record):
        return 0 
    
    current_character = record[0]

    if current_character == '.':
        return count_arrangements(record[1:], groups)
    
    elif current_character == '#':
        next_character = record[1:2]
        first_group_size = groups[0]

        if first_group_size == 1:
            if next_character == '#':
                return 0
            return count_arrangements('.' + record[2:], groups[1:])
        
        else:
            if next_character == '.':
                return 0 
            return count_arrangements('#' + record[2:], (first_group_size - 1,) + groups[1:])
        
    elif current_character == '?':
        return count_arrangements('.' + record[1:], groups
                                  ) + count_arrangements('#' + record[1:], groups)
    
    else:
        raise ValueError(f'Invalid character: {current_character}')
    

def main():
    folded_arrangements = 0
    unfolded_arrangements = 0

    with open("input.txt") as f:

        for line in f:
            record, group_str = line.strip().split(" ")
            groups = tuple(map(int, group_str.split(",")))

            folded_arrangements += count_arrangements(record, groups)
            unfolded_arrangements += count_arrangements('?'.join([record] * 5), groups * 5)
    
    print('Part 1 Solution:', folded_arrangements)
    print('Part 2 Solution:', unfolded_arrangements)
    
    return None

if __name__ == "__main__":
    main()