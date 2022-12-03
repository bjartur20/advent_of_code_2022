def part1():
    lowercase_offset = 96
    uppercase_offset = 64

    with open('day3/input.txt') as f:
        priority = 0
        for bag_raw in f.readlines():
            bag = bag_raw.strip()
            nr_of_items = len(bag)

            for item in bag[:nr_of_items//2]:
                if item in bag[nr_of_items//2:]:
                    if item.islower():
                        priority += ord(item) - lowercase_offset
                    else:
                        priority += ord(item) - uppercase_offset + 26
                    break

    return priority


def part2():
    ...

def main():
    print("Day 2")

    print(f"\tPart 1: {part1()}")
    # print(f"\tPart 2: {part2()}")

if __name__ == "__main__":
    main()
