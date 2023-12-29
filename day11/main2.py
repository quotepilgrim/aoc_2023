import sys
from numpy import rot90

infile = sys.argv[1]
data = []


def expand(lst):
    def add_rows(lst):
        result = []
        for i in lst:
            if "#" not in i:
                result.append(["!" for _ in i])
            else:
                result.append(i)
        return result

    result = add_rows(lst)
    result = add_rows(rot90(result))
    return rot90(result, axes=(1, 0))


def get_distance(g1, g2):
    top_edge = min(g1[0], g2[0])
    bottom_edge = max(g1[0], g2[0])
    left_edge = min(g1[1], g2[1])
    right_edge = max(g1[1], g2[1])

    h_exclams = list(data[0][left_edge:right_edge]).count("!")
    v_exclams = list(i[0] for i in data[top_edge:bottom_edge]).count("!")

    h = abs(g1[0] - g2[0])
    v = abs(g1[1] - g2[1])

    d = v + h + (h_exclams + v_exclams) * 99

    return d


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
