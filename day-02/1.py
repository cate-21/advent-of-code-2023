import re

def is_valid_subset(subset: str) -> bool:
    maximum_count = {'red': 12, 'green': 13, 'blue': 14}
    cubes = [s.strip().split(' ') for s in subset.split(',')]
    return all(int(count) <= maximum_count[colour] for count, colour in cubes)

def id_or_zero(game: str) -> int:
    game_id, subsets = game.split(':')
    game_id = re.search(r'\d+', game_id).group(0)
    subsets = subsets.split(';')

    if all(is_valid_subset(subset) for subset in subsets):
        return int(game_id)
    
    return 0

def main():
    with open("input.txt") as f:
        return sum(id_or_zero(game) for game in f)

if __name__ == "__main__":
    print(main())
