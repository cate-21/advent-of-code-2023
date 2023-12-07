def max_colour_product(subsets: list) -> int:
    max_colours = {'red': 0, 'green': 0, 'blue': 0}
    for subset in subsets:
        for count, colour in (cube.strip().split() for cube in subset.split(',')):
            max_colours[colour] = max(max_colours[colour], int(count))

    return max_colours['red'] * max_colours['green'] * max_colours['blue']

def main():
    summed_power = 0

    with open("input.txt") as f:
        for game in f:
            _, subsets = game.split(':')
            subsets = subsets.split(';')

            summed_power += max_colour_product(subsets)
        
    return summed_power

if __name__ == "__main__":
    print(main())