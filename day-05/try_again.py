import re
from functools import reduce

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

def return_new_range(boundary: list, mappings: list) -> list:
    overlap = []
    print('boundary', boundary)

    for mapping in mappings:
        print('mapping', mapping)
        if boundary[0] <= mapping[1] + mapping[2] and mapping[1] <= boundary[1]:
            print("should make it here")
            overlap.append([max(boundary[0], mapping[1]), min(boundary[1], mapping[1] + mapping[2])])

    overlap = sorted(overlap, key=lambda x: x[0])
    print('overlap', overlap)

    if overlap:
        remainder = [[boundary[0], overlap[0][0]]]

        for i in range(len(overlap) - 1):
            remainder.append([overlap[i][1], overlap[i+1][0]])

        remainder.append([overlap[-1][1], boundary[1]])

        remainder = [range_pair for range_pair in remainder if range_pair[0] != range_pair[1]]
        
        return sorted(overlap + remainder, key=lambda x: x[0])
    else:
        return [boundary]
    
def main():

    with open("baby.txt") as f:
        lines = f.readlines()

    seeds = [int(num) for num in re.findall(r'\d+', lines[0])]
    seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

    almanac = format_almanac(lines)

    seed_location = [1]
    seed_test = [[1, 200]]
    seed_soil_test = [[50, 98, 2], [52, 50, 48]]
    #seed_test = [[5, 12], [17, 24]]
    #seed_soil_test = [[24, 10, 5], [10, 24, 5]]
    seed_soil_test = [[0, 69, 1], [1, 0, 69]]

    print(return_new_range([55, 68], seed_soil_test))
    #for seed in seed_test:
        #for key in almanac.keys():
        #print(return_new_range(seed, seed_soil_test))
        #print('\n')


    return min(seed_location)
    
if __name__ == "__main__":
    print(main())