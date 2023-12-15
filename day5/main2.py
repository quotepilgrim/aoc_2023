import sys
import math

infile = sys.argv[1]
seeds = []
maps = {}

map_name = ""
with open(infile, "r") as f:
    for line in f:
        if "seeds" in line:
            seeds = [int(i) for i in line.split(":")[1].split()]
        elif "map" in line:
            map_name = line.split()[0].replace("-", "_")
            maps[map_name] = []
        elif line.strip() and ":" not in line:
            nums = [int(i) for i in line.split()]
            maps[map_name].append(tuple(nums))
        else:
            continue

seed_ranges = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]


def find_item(item, input_map):
    for mapping in input_map:
        dest_start, source_start, range_size = mapping
        if (item >= source_start) and (item < (source_start + range_size)):
            return dest_start + item - source_start
    return item


results = []
new_result = math.inf

# This is a HORRIBLE idea. Don't run this.

for seed_range in seed_ranges:
    for seed in range(seed_range[0], sum(seed_range)):
        result = seed
        for key in maps:
            result = find_item(result, maps[key])
        new_result = min(result, new_result)

print(new_result)
