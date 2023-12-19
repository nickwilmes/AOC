from aocd import data
import itertools


####################
# TEST DATA
####################
test_data = """\
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

test_a_answer = "374"
test_b_answer = "82000210"


####################
# Puzzle solutions
####################


def get_distance(
    map: list[list[int]], start: tuple[int, int], end: tuple[int, int]
) -> int:
    dist = 0
    while start != end:
        if start[0] < end[0]:
            start = (start[0] + 1, start[1])
        elif start[0] > end[0]:
            start = (start[0] - 1, start[1])
        elif start[1] < end[1]:
            start = (start[0], start[1] + 1)
        elif start[1] > end[1]:
            start = (start[0], start[1] - 1)
        dist += map[start[1]][start[0]]
    return dist


def part_a(content: str):
    data = content.split("\n")
    data = list(map(list, data))

    cost_map = []
    for y in range(len(data)):
        cost_map.append([])
        for x in range(len(data[0])):
            cost_map[y].append(1)

    for y, line in enumerate(data):
        if all([ch == "." for ch in line]):
            cost_map[y] = [ch + 1 for ch in cost_map[y]]

    for x in range(len(data[0])):
        all_dots = True
        for y in range(len(data)):
            if data[y][x] != ".":
                all_dots = False
                break

        if all_dots:
            for y in range(len(data)):
                cost_map[y][x] = cost_map[y][x] + 1

    galaxies = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch != ".":
                galaxies.append((x, y))

    pairs = list(itertools.combinations(galaxies, 2))

    dist = 0
    for start, end in pairs:
        dist += get_distance(cost_map, start, end)

    return dist


def part_b(content: str):
    data = content.split("\n")
    data = list(map(list, data))

    cost_map = []
    for y in range(len(data)):
        cost_map.append([])
        for x in range(len(data[0])):
            cost_map[y].append(1)

    for y, line in enumerate(data):
        if all([ch == "." for ch in line]):
            cost_map[y] = [ch * 1_000_000 for ch in cost_map[y]]

    for x in range(len(data[0])):
        all_dots = True
        for y in range(len(data)):
            if data[y][x] != ".":
                all_dots = False
                break

        if all_dots:
            for y in range(len(data)):
                cost_map[y][x] = cost_map[y][x] * 1_000_000

    galaxies = []
    for y, line in enumerate(data):
        for x, ch in enumerate(line):
            if ch != ".":
                galaxies.append((x, y))

    pairs = list(itertools.combinations(galaxies, 2))

    dist = 0
    for start, end in pairs:
        dist += get_distance(cost_map, start, end)

    return dist


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
