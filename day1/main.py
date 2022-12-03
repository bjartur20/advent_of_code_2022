def get_sum_of_all():
    all_elfs = []
    curr = 0
    with open('day1/input.txt') as f:
        for line in f.readlines():
            if not line.strip():
                all_elfs.append(curr)
                curr = 0
            else:
                curr += int(line.strip())

def part1():
    all_elves = get_sum_of_all()

    return max(all_elves)

def part2():
    all_elves = get_sum_of_all()

    return sum(sorted(all_elves, reverse=True)[0:3])

def main():
    print("Day 1")

    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
