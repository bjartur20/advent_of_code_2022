def read_file(filename):
    with open(filename) as f:
        lines = []
        for line in f.readlines():
            lines.append(line.strip())

    return lines