import re
from importlib import import_module

def apply_mapping(boundary: list, mapping: list) -> list:
    for map_dest, map_source, map_span in mapping:
        if map_source <= boundary[0] < map_source + map_span:
            return [map_dest + (boundary[0] - map_source), 
                    map_dest + (boundary[1] - map_source)]
    return boundary

def split_and_map(boundary: list, mappings: list) -> list:
    overlap = []

    boundary_start, boundary_end = boundary

    for _, map_source, map_span in mappings:
        
        if boundary_start <= map_source or boundary_end >= map_source + map_span:
            range_start = max(boundary_start, map_source)
            range_end = min(boundary_end, map_source + map_span)
            
            if range_start <= range_end:
                overlap.append([range_start, range_end])

    return [apply_mapping(x, mappings) for x in sorted(overlap, key=lambda x: x[0])
            ] if overlap else [
                apply_mapping(boundary, mappings)]
    
def main():

    with open("input.txt") as f:
        lines = f.readlines()

    seeds = [int(num) for num in re.findall(r'\d+', lines[0])]
    seed_ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]

    almanac = import_module('1').format_almanac(lines)

    all_location_ranges = []

    for seed in seed_ranges:
        current_ranges = [seed] 

        for key in almanac.keys():
            current_ranges = [range_item for current_range in current_ranges 
                              for range_item in split_and_map(current_range, almanac[key])]

        all_location_ranges.append(current_ranges)

    return min([location[0] for seed_location_ranges in all_location_ranges 
                for location in seed_location_ranges])
    
if __name__ == "__main__":
    print(main())