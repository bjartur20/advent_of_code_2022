def part1():
    all_elfs = []
    curr = 0
    with open('day1/input.txt') as f:
        for line in f.readlines():
            if not line.strip():
                all_elfs.append(curr)
                curr = 0
            else:
                curr += int(line.strip())

    return max(all_elfs)

def main():
    print("starting day 1...")

    print(part1())
