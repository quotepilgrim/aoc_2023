import sys

infile = sys.argv[1]
data = {}
name, values = ("", [])

with open(infile, "r") as f:
    for line in f:
        if line.strip():
            name, values = line.split(":")
            values = map(int, [i for i in values.split()])
        data[name] = list(values)

print(data)
