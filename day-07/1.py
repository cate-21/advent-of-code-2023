from collections import Counter
from functools import reduce

def sort_hands(hands_bids: list) -> list:

    TOTAL_TYPES = 7
    card_types = [[] for _ in range(TOTAL_TYPES)]
    ordered_types = [(5, 1), (4, 2), (3, 2), (3, 3), (2, 3), (2, 4), (1, 5)]
    
    for card, bid in hands_bids:
        card_counts = Counter(card).most_common()
        count_pattern = (card_counts[0][1], len(card_counts))

        for i, type_def in enumerate(ordered_types):
            if count_pattern == type_def:
                card_types[i].append((card, bid))
                break
    
    for card_type in card_types:
        card_type.sort(key=lambda hand: ["AKQJT98765432".index(card) for card in hand[0]])

    return list(reduce(lambda x, y: x + y, card_types))[::-1]

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    hands_bids = [(line.split(' ')[0], int(line.split(' ')[1].strip())) for line in lines]

    total_winnings = 0
    for i, (_, bid) in enumerate(sort_hands(hands_bids)):
        total_winnings += bid * (i + 1)

    return total_winnings

if __name__ == "__main__":
    print(main())