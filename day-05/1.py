import re

def next_value(start: int, mappings: list) -> int:
    for dest_start, source_start, span in mappings:
        if source_start <= start < source_start + span:
            return dest_start + (start - source_start)
        
    return start

def format_almanac(lines: str) -> dict:
    almanac = {}

    for line in lines[2:]:
        line = line.strip()

        if ':' in line:
            current_category = line.split(':')[0].strip()
            almanac[current_category] = []
        elif line and current_category:
            almanac[current_category].append([int(x) for x in line.split()])

    return almanac

def main():

    with open("input.txt") as f:
        lines = f.readlines()

    seeds = [int(num) for num in re.findall(r'\d+', lines[0])]
    almanac = format_almanac(lines)

    seed_location = []

    for seed in seeds:
        current_value = int(seed)

        for key in almanac.keys():
            current_value = next_value(current_value, almanac[key])
            
        seed_location.append(current_value)

    return min(seed_location)
    
if __name__ == "__main__":
    print(main())



