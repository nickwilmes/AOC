from aocd import data


####################
# TEST DATA
####################
test_data_a = """\
7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ"""

test_data_b = """\
FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L"""

test_a_answer = "8"
test_b_answer = "10"


####################
# Puzzle solutions
####################

Cord = tuple[int, int]


def get_next_step(prev: Cord, current: Cord, symbol: str) -> Cord:
    x, y = current
    if symbol == "|":
        neighbors = [(x, y - 1), (x, y + 1)]
    elif symbol == "-":
        neighbors = [(x - 1, y), (x + 1, y)]
    elif symbol == "L":
        neighbors = [(x, y - 1), (x + 1, y)]
    elif symbol == "J":
        neighbors = [(x, y - 1), (x - 1, y)]
    elif symbol == "7":
        neighbors = [(x, y + 1), (x - 1, y)]
    elif symbol == "F":
        neighbors = [(x, y + 1), (x + 1, y)]
    else:
        raise Exception(f"invalid {symbol=}")

    neighbors.remove(prev)
    return neighbors[0]


def part_a(content: str):
    map = content.split("\n")

    # find starting point
    start = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                start = (x, y)
                break

    # find connected neighbors
    neighbors = []
    x, y = start
    if y - 1 >= 0 and map[y - 1][x] in ["|", "F", "7"]:
        neighbors.append((x, y - 1))
    if y + 1 < len(map) and map[y + 1][x] in ["|", "L", "J"]:
        neighbors.append((x, y + 1))
    if x - 1 >= 0 and map[y][x - 1] in ["-", "L", "F"]:
        neighbors.append((x - 1, y))
    if x + 1 < len(map[0]) and map[y][x + 1] in ["-", "7", "J"]:
        neighbors.append((x + 1, y))

    # sanity check that only 2 neighbors exist
    if len(neighbors) != 2:
        raise Exception(f"incorrect number of {neighbors=}")

    # find farthest point
    prevs = [start, start]
    count = 1
    while neighbors[0] != neighbors[1]:
        count += 1
        temps = [
            get_next_step(
                prevs[0], neighbors[0], map[neighbors[0][1]][neighbors[0][0]]
            ),
            get_next_step(
                prevs[1], neighbors[1], map[neighbors[1][1]][neighbors[1][0]]
            ),
        ]
        prevs = neighbors
        neighbors = temps

    return count


def part_b(content: str):
    map = content.split("\n")
    for i in range(len(map)):
        map[i] = list(map[i])

    # find starting point
    start = (0, 0)
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == "S":
                start = (x, y)
                break

    # find connected neighbors
    neighbors = []
    possible_starts = "|-LFJ7"
    x, y = start
    if y - 1 >= 0 and map[y - 1][x] in ["|", "F", "7"]:
        neighbors.append((x, y - 1))
        possible_starts = (
            possible_starts.replace("-", "").replace("F", "").replace("7", "")
        )
    if y + 1 < len(map) and map[y + 1][x] in ["|", "L", "J"]:
        neighbors.append((x, y + 1))
        possible_starts = (
            possible_starts.replace("-", "").replace("L", "").replace("J", "")
        )
    if x - 1 >= 0 and map[y][x - 1] in ["-", "L", "F"]:
        neighbors.append((x - 1, y))
        possible_starts = (
            possible_starts.replace("|", "").replace("F", "").replace("L", "")
        )
    if x + 1 < len(map[0]) and map[y][x + 1] in ["-", "7", "J"]:
        neighbors.append((x + 1, y))
        possible_starts = (
            possible_starts.replace("|", "").replace("7", "").replace("J", "")
        )

    # sanity check that only 2 neighbors exist
    if len(neighbors) != 2 and len(possible_starts) != 1:
        raise Exception(f"incorrect number of {neighbors=} or {possible_starts=}")

    # replace start with correct symbol
    map[start[1]][start[0]] = possible_starts

    # mark path of loop
    prevs = [start, start]
    traveled = []
    for i in range(len(map)):
        traveled.append([" "] * len(map[0]))
    traveled[start[1]][start[0]] = "#"
    while neighbors[0] != neighbors[1]:
        temps = [
            get_next_step(
                prevs[0], neighbors[0], map[neighbors[0][1]][neighbors[0][0]]
            ),
            get_next_step(
                prevs[1], neighbors[1], map[neighbors[1][1]][neighbors[1][0]]
            ),
        ]
        traveled[neighbors[0][1]][neighbors[0][0]] = "#"
        traveled[neighbors[1][1]][neighbors[1][0]] = "#"
        prevs = neighbors
        neighbors = temps
    traveled[neighbors[0][1]][neighbors[0][0]] = "#"

    for y, line in enumerate(traveled):
        inside = False
        pre_turn = None
        for x, ch in enumerate(line):
            if ch == " ":
                traveled[y][x] = "I" if inside else "O"
            else:
                map_ch = map[y][x]
                if map_ch == "|":
                    inside = not inside
                elif map_ch in "FL":
                    pre_turn = map_ch
                elif map_ch == "7":
                    inside = inside if pre_turn == "F" else not inside
                    pre_turn = None
                elif map_ch == "J":
                    inside = inside if pre_turn == "L" else not inside
                    pre_turn = None

    for y in range(len(map)):
        print(f"{map[y]}     {traveled[y]}")

    traveled = ["".join(line) for line in traveled]
    return "\n".join(traveled).count("I")


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data_a)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data_b)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
