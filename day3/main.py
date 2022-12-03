def get_priority(item):
    lowercase_offset = 96
    uppercase_offset = 64
    if item.islower():
        return ord(item) - lowercase_offset
    
    return ord(item) - uppercase_offset + 26

def part1():
    with open('day3/input.txt') as f:
        priority = 0
        for bag_raw in f.readlines():
            bag = bag_raw.strip()
            nr_of_items = len(bag)

            for item in bag[:nr_of_items//2]:
                if item in bag[nr_of_items//2:]:
                    priority += get_priority(item)
                    break

    return priority


def part2():
    lowercase_offset = 96
    uppercase_offset = 64

    with open('day3/input.txt') as f:
        bags = f.readlines()
        priority = 0
        for idx in range(0, len(bags), 3):
            one, two, three = bags[idx].strip(), bags[idx + 1].strip(), bags[idx + 2].strip()

            for item in one:
                if item in two and item in three:
                    priority += get_priority(item)
                    break

    return priority

def main():
    print("Day 2")

    print(f"\tPart 1: {part1()}")
    print(f"\tPart 2: {part2()}")

if __name__ == "__main__":
    main()
