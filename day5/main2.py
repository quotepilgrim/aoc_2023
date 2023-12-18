import sys

infile = sys.argv[1]
seeds = []
maps = {}

map_name = ""
with open(infile, "r") as f:
    for line in f:
        if "seeds" in line:
            seeds = [int(i) for i in line.split(":")[1].split()]
        elif "map" in line:
            map_name = line.split()[0]
            maps[map_name] = []
        elif line.strip() and ":" not in line:
            nums = [int(i) for i in line.split()]
            maps[map_name].append(tuple(nums))
        else:
            continue

seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

print(seed_ranges, maps)

# It has become clear that if I'm going to solve this I'll have to restart
# pretty much from scratch. It may take a very long time until I finally come
# back to this with fresh eyes.
