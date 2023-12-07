import re

def main():
    total_sum = 0

    with open("input.txt") as f:
        for line in f:
            line = re.sub(r'\s+', ' ', line.strip())
            card_numbers, winning_numbers = map(lambda x: set(map(int, x.strip().split(' '))), 
                                                line.split(':')[1].split('|'))
            
            matches = len(card_numbers.intersection(winning_numbers))

            if matches:
                total_sum += pow(2, matches-1)
    
    return total_sum

if __name__ == "__main__":
    print(main())
        