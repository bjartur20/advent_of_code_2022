def part1():
    play_map = {
        "X": {
            "points": 1,
            "opponent": "A",
            "beats": "C",
        },
        "Y": {
            "points": 2,
            "opponent": "B",
            "beats": "A",
        },
        "Z": {
            "points": 3,
            "opponent": "C",
            "beats": "B",
        }
    }
    points = 0
    with open('day2/input.txt') as f:
        for line in f.readlines():
            elf, me = line.strip().split(" ")
            
            if elf == play_map[me]["opponent"]: # Draw
                points += 3
            elif elf == play_map[me]["beats"]: # Win
                points += 6
            
            points += play_map[me]["points"]

    return points

def part2():
    play_map = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1
        }
    }
    points = 0
    with open('day2/input.txt') as f:
        for line in f.readlines():
            elf, outcome = line.strip().split(" ")
            
            if outcome == "Y": # Draw
                points += 3
            elif outcome == "Z": # Win
                points += 6
            
            points += play_map[elf][outcome]

    return points

def main():
    print("Day 2")

    print(f"\tPart 1: {part1()}")
    print(f"\tPart 2: {part2()}")

if __name__ == "__main__":
    main()
