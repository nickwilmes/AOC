from aocd import data
import itertools


####################
# TEST DATA
####################
test_data = """\
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
"""
test_b_data = test_data
test_a_answer = "3749"
test_b_answer = "11387"


####################
# Puzzle solutions
####################
def add(a: int, b: int) -> int:
    return a+b


def mult(a: int, b: int) -> int:
    return a*b


def merge(a: int, b: int) -> int:
    return int(f"{a}{b}")


def is_possible(nums: list[int], value: int, operations) -> bool:
    oper_combos = list(itertools.product(operations, repeat=len(nums)-1))

    for op_list in oper_combos:
        result = nums[0]
        for i in range(len(op_list)):
            result = op_list[i](result, nums[i+1])
            if result > value:
                break
        
        if result == value:
            return True

    return False


def part_a(content):
    ans = 0
    operations = [add, mult]
    for line in content.splitlines():
        value = int(line.partition(':')[0])
        nums = [int(x) for x in line.partition(": ")[-1].split(' ')]

        if is_possible(nums, value, operations):
            ans += value
        
    return ans


def part_b(content):
    ans = 0
    operations = [add, mult, merge]
    for line in content.splitlines():
        value = int(line.partition(':')[0])
        nums = [int(x) for x in line.partition(": ")[-1].split(' ')]

        if is_possible(nums, value, operations):
            ans += value
        
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

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
