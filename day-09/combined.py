from itertools import accumulate

def main():

    forward_sum = 0
    backward_sum = 0

    with open("input.txt") as f:
        for line in f:

            sequence = [int(x) for x in line.split()]
            intermediate_sequences = [sequence]

            while not all(z == 0 for z in sequence) != 0:
                sequence = [y-x for x, y in zip(sequence[0:-1], sequence[1:])]
                intermediate_sequences.append(sequence)

            forward_sum += sum([sequence[-1] for sequence in intermediate_sequences[::-1]])

            backward_sum += list(accumulate(
                [sequence[0] for sequence in intermediate_sequences[::-1]], 
                lambda x, y: y - x))[-1]

    print('Part 1 Solution:', forward_sum)
    print('Part 2 Solution:', backward_sum)
    
    return None

if __name__ == "__main__":
    main()

