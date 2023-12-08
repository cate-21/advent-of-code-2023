from math import ceil, floor

def quadratic_solution(t: int, d: int) -> int:
    discriminant = t ** 2 - 4 * d

    if discriminant >= 0:
        x1 = (-t + discriminant ** 0.5) / -2
        x2 = (-t - discriminant ** 0.5) / -2

        return 1 + abs(ceil(x1) - floor(x2))
    else:
        return 1
    
def part_one(times: list, distances: int) -> int:
    product_variation = 1
    
    for t, d in zip(times, [distance + 1 for distance in distances]):
            product_variation *= quadratic_solution(t, d)

    return product_variation

def part_two(times: list, distances: int) -> int:
     
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))

    return quadratic_solution(time, distance + 1)

def main():
    with open("input.txt") as f:
        lines = f.readlines()

    times = [int(num) for num in lines[0].split() if num.isdigit()]
    distances = [int(num) for num in lines[1].split() if num.isdigit()]

    print('Part 1 Solution:', part_one(times, distances))
    print('Part 2 Solution:', part_two(times, distances))

    return None

if __name__ == "__main__":
    main()
    