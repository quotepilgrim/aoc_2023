import sys
import re

expr = "(.*) = \\((.*), (.*)\\)"

infile = sys.argv[1]
rule = ""
starts = []
ends = []

with open(infile) as f:
    rule = f.readline().strip()
    for line in f:
        if line.strip():
            s, *e = re.search(expr, line).groups()  # type: ignore
            starts.append(s)
            ends.append(e)

rule = [0 if i == "L" else 1 for i in rule]
rule_len = len(rule)

count, location = 0, "AAA"

while location != "ZZZ":
    location = ends[starts.index(location)][rule[count % rule_len]]
    count += 1

print(count)
