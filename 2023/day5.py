from typing import List
from aocd import data


####################
# TEST DATA
####################
test_data = """\
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""

test_a_answer = "35"
test_b_answer = "46"


####################
# Puzzle solutions
####################


def parse_map(data: List[str]) -> list[tuple[int, int, int]]:
    map = []
    for line in data[1::]:
        map.append([int(x) for x in line.split()])

    return map


def parse_input(lines: list[str]) -> dict:
    data = {}

    # parse seed list
    data["seeds"] = [int(x) for x in lines[0].partition(": ")[-1].split()]

    # break rest of input into maps
    maps_raw = []
    block = []
    for line in lines[2::]:
        if line == "":
            maps_raw.append(block)
            block = []
        else:
            block.append(line)
    maps_raw.append(block)

    # parse maps
    data["maps"] = []
    for map in maps_raw:
        data["maps"].append(parse_map(map))

    return data


def get_dest(map: list[tuple[int, int, int]], src: int) -> int:
    for line in map:
        map_dest, map_src, map_length = line
        min, max = map_src, map_src + map_length
        if src >= min and src <= max:
            return map_dest + (src - min)

    return src


def part_a(content: str):
    data = parse_input(content.split("\n"))

    # map seeds to locations
    seed_loc_map = {}
    for seed in data["seeds"]:
        id = seed
        for map in data["maps"]:
            id = get_dest(map, id)

        seed_loc_map[seed] = id

    return min(seed_loc_map.values())


def part_b(content):
    data = parse_input(content.split("\n"))

    # parse seeds differently
    seeds = []
    for i in range(0, len(data["seeds"]), 2):
        seeds.append((data["seeds"][i], data["seeds"][i] + data["seeds"][i + 1]))

    # map seed ranges to locations
    for map in data["maps"]:
        new = []
        while len(seeds) > 0:
            start, end = seeds.pop()
            for dest, src, length in map:
                overlap_start = max(start, src)
                overlap_end = min(end, src + length)
                if overlap_start < overlap_end:
                    new.append((overlap_start - src + dest, overlap_end - src + dest))
                    if overlap_start > start:
                        seeds.append((start, overlap_start))
                    if end > overlap_end:
                        seeds.append((overlap_end, end))
                    break
            else:
                new.append((start, end))
        seeds = new

    return min(seeds)[0]


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
