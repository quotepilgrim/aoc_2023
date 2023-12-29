import sys
from numpy import rot90

infile = sys.argv[1]
data = []


def expand(lst):
    def add_rows(lst):
        result = []
        for i in lst:
            result.append(i)
            if "#" not in i:
                result.append(i)
        return result
    result = add_rows(lst)
    result = add_rows(rot90(result))
    return rot90(result, k=3)


def get_distance(g1, g2):
    v = abs(g1[0] - g2[0])
    h = abs(g1[1] - g2[1])
    return v + h


with open(infile, "r") as f:
    for line in f:
        data.append(list(line.strip()))

data = expand(data)

galaxies = []
galaxy_num = 0

for i, line in enumerate(data):
    for j, char in enumerate(line):
        if char == "#":
            galaxy_num += 1
            galaxies.append((i, j, galaxy_num))

galaxy_pairs = set()
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2:
            galaxy_pairs.add(tuple(sorted((g1, g2))))

distances = [get_distance(*p) for p in galaxy_pairs]

print(sum(distances))
