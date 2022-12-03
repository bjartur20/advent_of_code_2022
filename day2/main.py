something = {
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


def get_points():
    points = 0
    with open('day2/input.txt') as f:
        for line in f.readlines():
            p1, p2 = line.strip().split(" ")
            
            if p1 == something[p2]["opponent"]: # Draw
                points += 3
            elif p1 == something[p2]["beats"]: # Win
                points += 6
            
            points += something[p2]["points"]

    return points


def part1():
    return get_points()

def main():
    print("Day 2")

    print(f"\tPart 1: {part1()}")
