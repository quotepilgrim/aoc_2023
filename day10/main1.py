import sys

infile = sys.argv[1]
data = []
row, col = 0, 0
start_row, start_col = 0, 0

with open(infile, "r") as f:
    for line in f:
        new_line = []
        for char in line.strip():
            if char == "-":
                new_line.append("we")
            elif char == "|":
                new_line.append("ns")
            elif char == "F":
                new_line.append("es")
            elif char == "7":
                new_line.append("ws")
            elif char == "J":
                new_line.append("nw")
            elif char == "L":
                new_line.append("ne")
            else:
                if char == "S":
                    start_row, start_col = row, col
                new_line.append("__")
            col += 1
        col = 0
        row += 1
        data.append(new_line)

start_point = []

if "s" in data[start_row - 1][start_col]:
    start_point.append("n")
if "w" in data[start_row][start_col + 1]:
    start_point.append("e")
if "n" in data[start_row + 1][start_col]:
    start_point.append("s")
if "e" in data[start_row][start_col - 1]:
    start_point.append("w")

data[start_row][start_col] = "".join(start_point)

seen = [(start_row, start_col)]
queue = [(start_row, start_col)]

while queue:
    current = queue.pop(0)
    try:
        if (
            (current[0] - 1, current[1]) not in seen
            and "s" in data[current[0] - 1][current[1]]
            and "n" in data[current[0]][current[1]]
        ):
            seen.append((current[0] - 1, current[1]))
            queue.append((current[0] - 1, current[1]))
    except IndexError:
        pass
    try:
        if (
            (current[0], current[1] + 1) not in seen
            and "w" in data[current[0]][current[1] + 1]
            and "e" in data[current[0]][current[1]]
        ):
            seen.append((current[0], current[1] + 1))
            queue.append((current[0], current[1] + 1))
    except IndexError:
        pass
    try:
        if (
            (current[0] + 1, current[1]) not in seen
            and "n" in data[current[0] + 1][current[1]]
            and "s" in data[current[0]][current[1]]
        ):
            seen.append((current[0] + 1, current[1]))
            queue.append((current[0] + 1, current[1]))
    except IndexError:
        pass
    try:
        if (
            (current[0], current[1] - 1) not in seen
            and "e" in data[current[0]][current[1] - 1]
            and "w" in data[current[0]][current[1]]
        ):
            seen.append((current[0], current[1] - 1))
            queue.append((current[0], current[1] - 1))
    except IndexError:
        pass

print(len(seen)/2)
