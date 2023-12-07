from functools import reduce

def find_adjacent_stars(x, y, lines):
    return [(x + i, y + j) for i in [-1, 0, 1] for j in [-1, 0, 1] 
            if (i != 0 or j != 0) 
            and 0 <= x + i < len(lines) 
            and 0 <= y + j < len(lines[0]) 
            and lines[x + i][y + j] == '*']

def sum_gear_ratios(lines):
    total_sum = 0
    star_to_num = {}
    digit_sequence = ""

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
                if char.isdigit():
                    digit_sequence += char
                else:
                    if digit_sequence:

                        adjacent_stars = list(set(
                            reduce(lambda x, y: x + y, 
                                   [find_adjacent_stars(i, j-d-1, lines) for d in range(len(digit_sequence))],
                                   [])))

                        for star in adjacent_stars:
                            if star in star_to_num:
                                total_sum += int(digit_sequence) * star_to_num[star]
                                del star_to_num[star]
                            else:
                                star_to_num[star] = int(digit_sequence)

                    digit_sequence = ""
    return total_sum


def main():
    with open("input.txt") as f:
        lines = [line for line in f]

    return sum_gear_ratios(lines)

if __name__ == "__main__":
    print(main())