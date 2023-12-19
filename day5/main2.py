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

seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]


def intersect(range_a, range_b):
    off_bounds = []
    intersection = []
    highest_lower_bound = max(range_a[0], range_b[0])
    lowest_upper_bound = min(range_a[1], range_b[1])

    if highest_lower_bound < lowest_upper_bound:
        intersection = (highest_lower_bound, lowest_upper_bound)
        if highest_lower_bound > range_a[0]:
            off_bounds.append((range_a[0], highest_lower_bound))
        if lowest_upper_bound < range_a[1]:
            off_bounds.append((lowest_upper_bound, range_a[1]))
    return intersection, off_bounds


results = []
for key in maps:
    map_ranges = maps[key]
    results = []
    while len(seed_ranges) > 0:
        seed_start, seed_end = seed_ranges.pop()
        for mapping in map_ranges:
            dest_start, source_start = mapping[:2]
            source_end = mapping[1] + mapping[2]

            intersection, off_bounds = intersect(
                (seed_start, seed_end), (source_start, source_end)
            )

            if intersection:
                intersection = [dest_start + i - source_start for i in intersection]
                results.append(tuple(intersection))
                for i in off_bounds:
                    seed_ranges.append(i)
                break
        else:
            results.append((seed_start, seed_end))
    seed_ranges = results

print(min(results)[0])
