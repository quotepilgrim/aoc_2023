import string
import sys

infile = sys.argv[1]
digits = string.digits

schematic = []
numbers = []
found_numbers = []

with open(infile, "r") as f:
    for line in f:
        schematic.append(line.strip())

height, width = len(schematic), len(schematic[0])


def find_asterisk(number, row, col):
    coords = [(row, col + i) for i in range(len(number))]
    for coord in coords:
        row, col = coord
        neighbors = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ]
        for neighbor in neighbors:
            row, col = neighbor
            out_of_bounds = (row < 0) or (col < 0) or (row >= height) or (col >= width)
            if not out_of_bounds and schematic[row][col] == "*":
                return row, col
    return -1, -1


row, col = 0, 0
while row < height:
    col = 0
    while col < width:
        current_number = ""
        current_coords = (0, 0)
        if schematic[row][col] in digits:
            current_coords = (row, col)
            while True:
                current_number += schematic[row][col]
                col += 1
                if col == width or schematic[row][col] not in digits:
                    break
            numbers.append((current_number, *current_coords))
        col += 1
    row += 1

del row, col

for i in numbers:
    asterisk_coords = find_asterisk(*i)
    if asterisk_coords[0] != -1:
        found_numbers.append((i[0], *asterisk_coords))

gear_candidates = [[i[1], i[2]] for i in found_numbers]
gears = []

for i in gear_candidates:
    if gear_candidates.count(i) == 2 and i not in gears:
        gears.append(i)

for gear in gears:
    for i in found_numbers:
        if gear[0:2] == [i[1], i[2]]:
            gear.append(int(i[0]))

gear_ratios = [(i[2] * i[3]) for i in gears]

print(sum(gear_ratios))
