from aocd import data
from typing import List


####################
# TEST DATA
####################
test_data = """\
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

test_a_answer = "4361"
test_b_answer = "467835"


####################
# Puzzle solutions
####################


def neighbor_symbols(lines: List[str], x: int, y: int, size: int) -> bool:
    # Check row above
    target_x, target_y = x - size - 1, y - 1
    if target_y >= 0:
        for i in range(size + 2):
            if target_x + i >= 0 and target_x + i < len(lines[0]):
                c = lines[target_y][target_x + i]
                if not c.isdigit() and c != ".":
                    return True

    # Check current row
    target_x, target_y = x - size - 1, y
    for i in range(size + 2):
        if target_x + i >= 0 and target_x + i < len(lines[0]):
            c = lines[target_y][target_x + i]
            if not c.isdigit() and c != ".":
                return True

    # check row below
    target_x, target_y = x - size - 1, y + 1
    if target_y < len(lines):
        for i in range(size + 2):
            if target_x + i >= 0 and target_x + i < len(lines[0]):
                c = lines[target_y][target_x + i]
                if not c.isdigit() and c != ".":
                    return True

    return False


def part_a(content: str):
    lines = content.split("\n")
    ans = 0

    for y in range(len(lines)):
        line = lines[y]
        cur_num = ""
        for x in range(len(line)):
            if line[x].isdigit():
                cur_num += line[x]
            elif len(cur_num) > 0:
                if neighbor_symbols(lines, x, y, len(cur_num)):
                    ans += int(cur_num)
                cur_num = ""

        if len(cur_num) > 0:
            if neighbor_symbols(lines, x, y, len(cur_num)):
                ans += int(cur_num)
            cur_num = ""

    return ans


class NotAGearException(Exception):
    pass


def get_gear_ratio(lines: List[str], x: int, y: int) -> int:
    nums = []

    if y > 0:
        nums.extend(get_neighbor_line_nums(lines[y - 1], x))

    if y < len(lines) - 1:
        nums.extend(get_neighbor_line_nums(lines[y + 1], x))

    num = get_left_num(lines[y], x)
    if num.isdigit():
        nums.append(num)
    num = get_right_num(lines[y], x)
    if num.isdigit():
        nums.append(num)

    if len(nums) != 2:
        raise NotAGearException(f"only has {len(nums)} numbers")

    return int(nums[0]) * int(nums[1])


def get_neighbor_line_nums(line: str, x: int) -> List[str]:
    nums = []
    left = get_left_num(line, x)
    right = get_right_num(line, x)

    # check if nums are connected
    if line[x].isdigit():
        nums.append(f"{left}{line[x]}{right}")
    else:
        if left.isdigit():
            nums.append(left)
        if right.isdigit():
            nums.append(right)

    return nums


def get_left_num(line: str, x: int) -> str:
    num = ""
    if x == 0:
        return num

    for i in range(x - 1, -1, -1):
        if line[i].isdigit():
            num = line[i] + num
        else:
            break

    return num


def get_right_num(line: str, x: int) -> str:
    num = ""
    if x == len(line) - 1:
        return num

    for i in range(x + 1, len(line), 1):
        if line[i].isdigit():
            num = num + line[i]
        else:
            break

    return num


def part_b(content):
    lines = content.split("\n")

    ratios = []

    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] != "*":
                continue

            try:
                ratios.append(get_gear_ratio(lines, x, y))
            except NotAGearException:
                continue

    return sum(ratios)


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
