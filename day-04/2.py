import re

def main():
    with open("input.txt") as f:
        cards = [re.sub(r'\s+', ' ', line.strip()) for line in f]
    
    counts = [1 for _ in cards]

    for i, card in enumerate(cards):
        card_numbers, winning_numbers = map(lambda x: set(map(int, x.strip().split(' '))), 
                                    card.split(':')[1].split('|'))
        consecutive_matches = len(card_numbers.intersection(winning_numbers))

        for j in range(i + 1, i + 1 + consecutive_matches):
            if j < len(cards): 
                counts[j] += counts[i]
    
    return sum(counts)

if __name__ == "__main__":
    print(main())