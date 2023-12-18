from aocd import data
from math import gcd


####################
# TEST DATA
####################
test_data = """\
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

test_data_b = """\
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

test_a_answer = "6"
test_b_answer = "6"


####################
# Puzzle solutions
####################

History = tuple[list[str], int]


def part_a(content: str):
    directions, maps_raw = content.split("\n\n")

    maps_raw = maps_raw.split("\n")
    maps = {}
    for line in maps_raw:
        name, dest = line.split(" = ")
        dest = dest.replace("(", "").replace(")", "")
        dest = dest.split(", ")
        maps[name] = dest

    pos = "AAA"
    count = 0
    while pos != "ZZZ":
        if directions[count % len(directions)] == "L":
            d = 0
        else:
            d = 1
        pos = maps[pos][d]
        count += 1

    return count


def get_loop(start: str, maps: dict, directions: str) -> tuple[list[History], int]:
    history = []
    i = 0
    dir_length = len(directions)
    dir_index = i % dir_length
    direction = 0 if directions[dir_index] == "L" else 1
    cache = {}
    while i < dir_length or (start, dir_index) not in cache:
        history.append((start, direction))
        cache[(start, dir_index)] = 0
        i += 1
        start = maps[start][direction]
        dir_index = i % dir_length
        direction = 0 if directions[dir_index] == "L" else 1

    loop_size = len(history) - history.index((start, direction))
    return (history, loop_size)


def check_step(i: int, paths: list[History]) -> bool:
    for path, loop_size in paths:
        loop_start = len(path) - loop_size
        if i <= loop_start:
            path_i = i
        else:
            path_i = loop_start + ((i - loop_start) % loop_size)
        if not path[path_i][0].endswith("Z"):
            return False
    return True


def part_b(content: str):
    directions, maps_raw = content.split("\n\n")

    maps_raw = maps_raw.split("\n")
    maps = {}
    for line in maps_raw:
        name, dest = line.split(" = ")
        dest = dest.replace("(", "").replace(")", "")
        dest = dest.split(", ")
        maps[name] = dest

    # build list of starting nodes
    pos_arr = []
    for node in maps.keys():
        if node.endswith("A"):
            pos_arr.append(node)

    pos_paths = []
    for pos in pos_arr:
        pos_paths.append(get_loop(pos, maps, directions))

    # sanity check to make sure every path has at least one exit
    for p, _ in pos_paths:
        exits = list(filter(lambda x: x[0].endswith("Z"), p))
        if len(exits) == 0:
            raise Exception(f"No exit for {p=}")

    # lcm method
    nums = [pos_path[1] for pos_path in pos_paths]
    lcm = nums.pop()

    for num in nums:
        lcm = lcm * num // gcd(lcm, num)

    return lcm


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data_b)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
