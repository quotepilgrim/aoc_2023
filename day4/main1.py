import re

infile = "input"
data = []

with open(infile, "r") as f:
    for line in f:
        data.append(line)

pattern = ".*:(.*)\\|(.*)"
re_matches = [re.search(pattern, i) for i in data]

games = [[i.group(1).split(), i.group(2).split()] for i in re_matches]  # type: ignore
results = []

for game in games:
    matches = [i for i in game[0] if i in game[1]]
    results.append(2 ** (len(matches) - 1) if len(matches) > 0 else 0)

print(sum(results))
