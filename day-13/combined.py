def find_reflection(pattern: list[str], diff: int) -> str:
    for i in range(1, len(pattern[0])):
        
        non_matching = sum(l != r for line in pattern 
                           for l, r in zip(reversed(line[:i]), line[i:]))
        
        if non_matching == diff:
            return i
        
    return 0

def summarise_pattern(pattern: list[str], diff: int = 0) -> int:
    vertical_reflection = find_reflection(pattern, diff)
    horizontal_transpose = list(zip(*pattern))
    
    return vertical_reflection if vertical_reflection \
        else 100 * find_reflection(horizontal_transpose, diff)

def main():

    with open("input.txt") as input:
        patterns = [pattern.split('\n') for pattern in input.read().split('\n\n')]
     
    print('Part 1 Solution:', sum(summarise_pattern(pattern)
                                  for pattern in patterns))
    print('Part 2 Solution:', sum(summarise_pattern(pattern, 1)
                                  for pattern in patterns))
    
    return None

if __name__ == "__main__":
    main()