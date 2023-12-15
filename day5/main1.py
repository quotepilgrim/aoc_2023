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
            map_name = line.split()[0].replace("-", "_")
            maps[map_name] = []
        elif line.strip() and ":" not in line:
            nums = [int(i) for i in line.split()]
            maps[map_name].append(tuple(nums))
        else:
            continue


def find_item(item, input_map):
    for mapping in input_map:
        dest_start, source_start, range_size = mapping
        if item in range(source_start, source_start + range_size):
            return dest_start + item - source_start
    return item


results = []

for seed in seeds:
    result = seed
    for key in maps:
        result = find_item(result, maps[key])
    results.append(result)

print(min(results))
