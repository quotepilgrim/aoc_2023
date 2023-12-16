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

seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]


def intersect(range_a, range_b, debug=False):
    off_bounds = []
    lowest_lower_bound = min(range_a[0], range_b[0])
    highest_lower_bound = max(range_a[0], range_b[0])
    lowest_upper_bound = min(range_a[1] - 1, range_b[1] - 1)
    highest_upper_bound = max(range_a[1] - 1, range_b[1] - 1)

    intersection = (highest_lower_bound, lowest_upper_bound)

    if intersection[0] > intersection[1]:
        if debug:
            print(f"Ranges:{range_a}, {range_b}")
        return range_a, range_b
    if lowest_lower_bound < intersection[0]:
        off_bounds.append((lowest_lower_bound, intersection[0]))
    if highest_upper_bound > intersection[1]:
        off_bounds.append((intersection[1], highest_upper_bound))
    if debug:
        print(f"Intersecton: {intersection}; off-bounds: {off_bounds}")
    return intersection, *off_bounds


def find_item(item, source_range, dest_range):
    if item in range(source_range[0], source_range[1]):
        return dest_range[0] + item - source_range[0]
    return item


results = []

for key in maps:
    for map_range in maps[key]:
        source_range = (map_range[1], map_range[1] + map_range[2])
        dest_range = (map_range[0], map_range[0] + map_range[2])
        for seed_range in seed_ranges:
            intersections = intersect(seed_range, source_range)
            for i in intersections:
                print(i)

print(results)
