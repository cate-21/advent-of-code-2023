from typing import Tuple, Union, List

def expansion_offset(
        universe_grid: Union[List[List[str]], List[Tuple[str, ...]]], 
        expansion_factor: int
        ) -> List[int]:
    
    row_offset = [0] * len(universe_grid)

    for i in range(len(universe_grid)):
        if i > 0:
            row_offset[i] = row_offset[i - 1]
        if all(cell == '.' for cell in universe_grid[i]):
            row_offset[i] += expansion_factor
    
    return row_offset

def galaxy_coordinates(
        universe_grid: List[List[str]], 
        expansion_factor: int
        ) -> List[Tuple[int, int]]:
    
    horizontal_offset = expansion_offset(universe_grid, expansion_factor)
    vertical_offset = expansion_offset(list(zip(*universe_grid)), expansion_factor)
    
    return [(i + horizontal_offset[i], j + vertical_offset[j])
            for i, row in enumerate(universe_grid) 
            for j, cell in enumerate(row) if cell == '#']

def get_pairs(coordinates: List[Tuple[int, int]]) -> List[List[Tuple[int, int]]]:
    return [[coordinates[i], coordinates[j]] 
            for i in range(len(coordinates)) 
            for j in range(i + 1, len(coordinates))]

def manhattan_distance(x1: int, y1: int, x2: int, y2: int) -> int:
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    with open("input.txt") as f:
        lines = [list(line.strip()) for line in f.readlines()]

    print('Part 1 Solution:', sum(manhattan_distance(x1, y1, x2, y2) 
                                  for (x1, y1), (x2, y2) in 
                                  get_pairs(galaxy_coordinates(lines, 1))))
    
    print('Part 2 Solution:', sum(manhattan_distance(x1, y1, x2, y2) 
                                  for (x1, y1), (x2, y2) in 
                                  get_pairs(galaxy_coordinates(lines, 999999))))

    return None

if __name__ == "__main__":
    main()