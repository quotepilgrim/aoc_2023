import sys
import re
import math

expr = "(.*) = \\((.*), (.*)\\)"

infile = sys.argv[1]
rule = ""
points = []
endpoints = []

with open(infile) as f:
    rule = f.readline().strip()
    for line in f:
        if line.strip():
            s, *e = re.search(expr, line).groups()  # type: ignore
            points.append(s)
            endpoints.append(e)

rule = [0 if i == "L" else 1 for i in rule]
rule_len = len(rule)

starts = {i: 0 for i in points if i[2] == "A"}

for k in starts:
    location = k
    while location[2] != "Z":
        location = endpoints[points.index(location)][rule[starts[k] % rule_len]]
        starts[k] += 1

print(math.lcm(*[starts[k] for k in starts]))
