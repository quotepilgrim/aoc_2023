import sys

infile = sys.argv[1]
inlists = {}

with open(infile, "r") as f:
    i = 0
    for line in f:
        inlists[i] = [[int(i) for i in line.strip().split()]]
        i += 1

for k in inlists:
    while not all(i == 0 for i in inlists[k][-1]):
        old_list = inlists[k][-1]
        new_list = [old_list[i+1] - old_list[i] for i in range(len(old_list)-1)]
        inlists[k].append(new_list)

for k in inlists:
    for i in inlists[k]:
        i.append(0)
    for i in range(1, len(inlists[k]) + 1):
        inlists[k][-i][-1] = inlists[k][-i][-2] + inlists[k][-i + 1][-1]

result = 0
for k in inlists:
    result += inlists[k][0][-1]

print(inlists, result)
