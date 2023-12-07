import re

NUMBER_WORDS = [
    "one", 
    "two", 
    "three", 
    "four", 
    "five", 
    "six", 
    "seven", 
    "eight", 
    "nine"]

def get_first_digit(line: str) -> str:
    subbed = re.sub('|'.join(NUMBER_WORDS), lambda x: str(NUMBER_WORDS.index(x.group()) + 1), line)
    return re.search(r'\d', subbed).group()

def get_last_digit(line: str) -> str:
    reverse_substiution = [x[::-1] for x in NUMBER_WORDS]
    subbed = re.sub('|'.join(reverse_substiution), 
                    lambda x: str(reverse_substiution.index(x.group()) + 1), line[::-1])
    return re.search(r'\d', subbed).group()

def main():
    calibration_sum = 0

    with open("input.txt") as f:
        for line in f:
            calibration_sum += int(get_first_digit(line) + get_last_digit(line))
    
    return calibration_sum

if __name__ == "__main__":
    print(main())
