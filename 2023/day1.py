from aocd import data


####################
# TEST DATA
####################
test_data = """\
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

test_b_data = """\
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
test_a_answer = "142"
test_b_answer = "281"


####################
# Puzzle solutions
####################


def get_num_part_a(s: str) -> int:
    first, last = "", ""
    for c in s:
        if c.isdigit():
            first = c
            break

    for c in s[::-1]:
        if c.isdigit():
            last = c
            break

    if first == "" or last == "":
        raise Exception(f"error parsing line: {s}")

    return int(f"{first}{last}")


def get_num_part_b(s: str) -> int:
    first, last = "", ""
    options = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }
    for i in range(len(s)):
        for opt in options.keys():
            if s[i::].startswith(opt):
                first = str(options[opt])
                break
        if first:
            break

    for i in range(len(s), -1, -1):
        for opt in options.keys():
            if s[i::].startswith(opt):
                last = str(options[opt])
                break
        if last:
            break

    if first == "" or last == "":
        raise Exception(f"error parsing line: {s}")

    return int(f"{first}{last}")


def part_a(content: str):
    lines = content.split("\n")
    total = 0

    for line in lines:
        num = get_num_part_a(line)
        total += num

    return total


def part_b(content):
    lines = content.split("\n")
    total = 0

    for line in lines:
        num = get_num_part_b(line)
        total += num

    return total


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_b_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
