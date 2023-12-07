def check_adjacent_cells(x: int, y: int, lines: list) -> bool:
    return any(
        (0 <= x + i < len(lines) and 0 <= y + j < len(lines[0]) and
         not lines[x + i][y + j].isdigit() 
         and lines[x + i][y + j] != '.' 
         and lines[x + i][y + j] != '\n')
        for i in [-1, 0, 1] for j in [-1, 0, 1] if not (i == 0 and j == 0)
    )

def sum_part_numbers(lines: list) -> int:
    total_sum = 0
    digit_sequence = ""

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char.isdigit():
                digit_sequence += char
            else:
                if digit_sequence and any(check_adjacent_cells(i, j-d-1, lines) for d in range(len(digit_sequence))):
                    total_sum += int(digit_sequence)
                digit_sequence = ""
    
    return total_sum

def main():
    with open("input.txt") as f:
        lines = [list(line) for line in f]

    return sum_part_numbers(lines)

if __name__ == "__main__":
    print(main())


