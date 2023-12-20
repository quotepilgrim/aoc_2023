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


def calculate(time, speed, record):
    remaining = time - speed
    distance = speed * remaining
    return distance > record


time = data["Time"]
dist = data["Distance"]

low = 0
mid = 0
high = time

while low < high:
    mid = low + (high - low) // 2
    if calculate(time, mid, dist):
        high = mid
    else:
        low = mid + 1

print(time + 1 - mid * 2)
