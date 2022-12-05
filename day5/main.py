def get_crates(input_data):
    crates_dict = {}
    for line_raw in input_data:
        if line_raw.startswith(" "):
            break
        line = line_raw.strip().split(" ")
        empty_count = 0
        idx = 1
        for crate in line:
            if crate:
                if crates_dict.get(idx):
                    crates_dict[idx].append(crate.strip("[]"))
                else:
                    crates_dict[idx] = [crate.strip("[]")]
                idx += 1
            else:
                empty_count += 1
                if empty_count == 4:
                    empty_count = 0
                    idx += 1

    return crates_dict


def get_moves(input_data):
    moves = []
    for line_raw in input_data:
        line = line_raw.strip()
        if line.startswith("move"):
            number, from_row, to_row = list(filter(str.isdigit, line.split()))
            moves.append(
                {"number": int(number), "from": int(from_row), "to": int(to_row)}
            )

    return moves


def part1():
    with open("day5/input.txt") as f:
        lines = f.readlines()
    crates = get_crates(lines)
    moves = get_moves(lines)

    for move in moves:
        crates[move["to"]] = (
            crates[move["from"]][: move["number"]][::-1] + crates[move["to"]]
        )
        crates[move["from"]] = crates[move["from"]][move["number"] :]

    return "".join([crates[key][0] for key in sorted(crates)])


def part2():
    ...


def main():
    print("Day 5")

    print(f"\tPart 1: {part1()}")
    print(f"\tPart 2: {part2()}")


if __name__ == "__main__":
    main()
