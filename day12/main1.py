import sys

infile = sys.argv[1]
data = []

with open(infile, "r") as f:
    for line in f:
        l, r = line.strip().split()
        data.append([list(l), r.split(",")])

print(*[''.join(i[0]) + ' ' + ','.join(i[1]) for i in data], sep="\n")
