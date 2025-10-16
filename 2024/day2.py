from aocd import data
from collections import defaultdict


####################
# TEST DATA
####################
test_data = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9"""

test_b_data = test_data
test_a_answer = "2"
test_b_answer = "4"


####################
# Puzzle solutions
####################


def check_report_safety_a(report: str) -> bool:
    nums = []
    for n in report.split():
        nums.append(int(n))
    
    ascending = (nums[0] < nums[1])

    if not ascending:
        nums.reverse()

    for i in range(1, len(nums)):
        n1 = nums[i-1]
        n2 = nums[i]
        if not check_2_nums(n1, n2, True):
            return False
        
    return True


def check_2_nums(n1: int, n2: int, asc: bool) -> bool:
    if asc:
        if n1 >= n2:
            return False
        if n2-n1 > 3:
            return False
    else:
        if n2 >= n1:
            return False
        if n1-n2 > 3:
            return False
        
    return True


def check_report_safety_b(nums: list[int], safety_triggered: bool = False) -> bool:
    
    ascending = (nums[0] < nums[1])

    for i in range(1, len(nums)):
        n1 = nums[i-1]
        n2 = nums[i]
        result = check_2_nums(n1, n2, ascending)
        
        if not result:
            if not safety_triggered:
                for j in range(i+1):
                    new_nums = nums[:j] + nums[j+1:]
                    if check_report_safety_b(new_nums, True):
                        return True
                return False
            else:
                return False
    return True


def part_a(content: str):
    lines = content.split("\n")

    count = 0
    for line in lines:
        if check_report_safety_a(line):
            count += 1

    return count


def part_b(content):
    lines = content.split("\n")

    count = 0
    for line in lines:
        nums = []
        for n in line.split():
            nums.append(int(n))
        if check_report_safety_b(nums):
            count += 1

    return count


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