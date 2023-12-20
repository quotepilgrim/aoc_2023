import sys

infile = sys.argv[1]
data = {}
name, value = ("", "")

with open(infile, "r") as f:
    for line in f:
        if line.strip():
            name, value = line.split(":")
            value = value.replace(" ", "").strip()
        data[name] = int(value)


def calculate(time, hold, record):
    speed = hold
    remaining = time - hold
    distance = speed * remaining
    return distance > record


time = data["Time"]
dist = data["Distance"]

hold = 0
while hold < time:
    hold += 1
    if calculate(time, hold, dist):
        break

print(time + 1 - hold * 2)
