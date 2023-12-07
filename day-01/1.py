import re

def main():
    calibration_sum = 0
    with open("input.txt") as f:
        for line in f:
            first_digit = re.search(r'\d', line).group()
            last_digit = re.search(r'\d', line[::-1]).group()
            calibration_sum += int(first_digit + last_digit)
    
    return calibration_sum

if __name__ == "__main__":
    print(main())