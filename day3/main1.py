import string
import sys

infile = sys.argv[1]
digits = string.digits

schematic = []
numbers = []
valid_numbers = []

with open(infile, "r") as f:
    for line in f:
        schematic.append(line.strip())

height, width = len(schematic), len(schematic[0])


def is_symbol(char):
    return char not in digits + "."


def find_neighbors(number, row, col):
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
            if not out_of_bounds and is_symbol(schematic[row][col]):
                return True
    return False


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
    if find_neighbors(*i):
        valid_numbers.append(int(i[0]))

print(sum(valid_numbers))
