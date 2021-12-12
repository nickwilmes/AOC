from aocd import data
import sys
from dataclasses import dataclass
import timeit


####################
# TEST DATA
####################
test_data = """\
16,1,2,0,4,2,7,1,2,14
"""
test_a_answer = "37"
test_b_answer = "168"


####################
# Puzzle solutions
####################
def part_a(content):
    content = list(map(int, content))
    content.sort()
    lowest_fuel = sys.maxsize
    for i in range(content[0], content[-1]):
        fuel = sum(list(map(lambda x: abs(x-i), content)))
        if fuel < lowest_fuel:
            lowest_fuel = fuel
    
    return lowest_fuel


def calc_cost(crab: int, dest: int):
    # return sum(range(abs(crab-dest)+1))
    n = abs(crab-dest)
    a = 1
    l = abs(crab-dest)
    return (n*(a+l))/2


def part_b(content=None):
    if not content:
        content = data.split(',')
    content = list(map(int, content))
    content.sort()
    
    min_pos, max_pos = content[0], content[-1]
    costs = { i : 0 for i in range(min_pos, max_pos)}
    for crab in content:
        for i in range(min_pos, max_pos):
            costs[i] += calc_cost(crab, i)
    
    values = list(costs.values())
    return int(min(values))


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.split(',')

    test_a = part_a(test_data.split(','))
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.split(','))
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")  # 95476248 is too high
    assert str(test_b) == test_b_answer

    # print(timeit.timeit('part_b()', "from __main__ import part_b", number=1))
