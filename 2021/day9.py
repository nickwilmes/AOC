from aocd import data
from typing import List
import math


####################
# TEST DATA
####################
test_data = """\
2199943210
3987894921
9856789892
8767896789
9899965678
"""
test_a_answer = "15"
test_b_answer = "1134"


####################
# Puzzle solutions
####################
def find_low_points(grid: List[List[str]]) -> List[tuple]:
    low_points = []
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            height = int(grid[row][col])
            if row > 0:
                if int(grid[row-1][col]) <= height:  # above
                    continue
            if row < len(grid)-1:
                if int(grid[row+1][col]) <= height:  # below
                    continue
            if col > 0:
                if int(grid[row][col-1]) <= height:  # left
                    continue
            if col < len(grid[row])-1:
                if int(grid[row][col+1]) <= height:  # right
                    continue
            low_points.append((row, col, height))
    return low_points


def part_a(content):
    return sum(list(map(lambda x: x[2]+1, find_low_points(content))))


def calculate_basin_size(starting_point: tuple, grid: List[List[str]]) -> int:
    process = set([starting_point])
    done = set()
    while len(process) > 0:
        row, col, height = process.pop()
        if row > 0:
            up = (row-1, col, int(grid[row-1][col]))
            if up[2] != 9 and up not in done:
                process.add(up)
        if row < len(grid)-1:
            down = (row+1, col, int(grid[row+1][col]))
            if down[2] != 9 and down not in done:
                process.add(down)
        if col > 0:
            left = (row, col-1, int(grid[row][col-1]))
            if left[2] != 9 and left not in done:
                process.add(left)
        if col < len(grid[row])-1:
            right = (row, col+1, int(grid[row][col+1]))
            if right[2] != 9 and right not in done:
                process.add(right)
        done.add((row, col, height))
    
    return len(done)


def part_b(content):
    low_points = find_low_points(content)

    sizes = []
    for low_point in low_points:
       sizes.append(calculate_basin_size(low_point, content))

    return math.prod(sorted(sizes, reverse=True)[0:3])


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")  # 1775 too high
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.splitlines())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
