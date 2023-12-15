import sys

infile = sys.argv[1]

with open(infile, "r") as f:
    for line in f:
        print(line.rstrip())
