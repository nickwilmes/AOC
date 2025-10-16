from aocd import data
from collections import defaultdict
import re

####################
# TEST DATA
####################
test_data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""

test_b_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
test_a_answer = "161"
test_b_answer = "48"


####################
# Puzzle solutions
####################
def process_mul(cmd: str) -> int:
    nums = cmd.partition('(')[-1].rpartition(')')[0].split(',')
    return int(nums[0])*int(nums[1])


def part_a(content: str):
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    matches = re.findall(pattern, content)
    ans = 0
    for match in matches:
        ans += process_mul(match)

    return ans


def part_b(content):
    pattern = r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))"

    matches = re.findall(pattern, content)
    ans = 0
    do = True
    for match in matches:
        if match == 'do()':
            do = True
        elif match == "don't()":
            do = False
        elif do:
            ans += process_mul(match)

    return ans


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