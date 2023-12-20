import sys
import math

infile = sys.argv[1]
data = {}
name, values = ("", [])

with open(infile, "r") as f:
    for line in f:
        if line.strip():
            name, values = line.split(":")
            values = map(int, values.split())
        data[name] = list(values)


def calculate(time, hold, record):
    speed = hold
    remaining = time - hold
    distance = speed * remaining
    return distance > record


race_wins = []

for i in range(len(data["Time"])):
    time = data["Time"][i]
    dist = data["Distance"][i]

    hold = 0
    wins = 0
    while hold < time:
        hold += 1
        if calculate(time, hold, dist):
            wins = time + 1 - hold * 2
            break
    race_wins.append(wins)

print(math.prod(race_wins))
