from collections import Counter
from functools import reduce

def sort_hands(hands_bids: list) -> list:

    TOTAL_TYPES = 7
    card_types = [[] for _ in range(TOTAL_TYPES)]
    ordered_types = [(5, 1), (4, 2), (3, 2), (3, 3), (2, 3), (2, 4), (1, 5)]
    
    for card, bid in hands_bids:

        card_counts = Counter(card)

        joker_count = card_counts.pop('J', 0)
        counts_excluding_joker = card_counts.most_common()
        
        for i, (max_count, type_len) in enumerate(ordered_types):
            if counts_excluding_joker:
                current_count, current_len = counts_excluding_joker[0][1], len(counts_excluding_joker)
                adjusted_count = min(current_count + joker_count, max_count)

                if (adjusted_count, current_len) == (max_count, type_len):
                    card_types[i].append((card, bid))
                    break
            else:
                card_types[i].append((card, bid))
                break
    
    for card_type in card_types:
        card_type.sort(key=lambda hand: ["AKQT98765432J".index(card) for card in hand[0]])

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