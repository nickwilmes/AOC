from aocd import data
from dataclasses import dataclass


####################
# TEST DATA
####################
test_data = """\
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""
test_a_answer = "1656"
test_b_answer = "195"


####################
# Puzzle solutions
####################
def process_step(grid: list):
    flashing = set()
    for y, row in enumerate(grid):
        for x, col in enumerate(row):
            grid[y][x] += 1
            if grid[y][x] > 9:
                flashing.add((x, y))
    
    flashed = set()
    while len(flashing) > 0:
        x, y = flashing.pop()
        neighbors = [
            (x-1, y-1), (x, y-1), (x+1, y-1),
            (x-1, y), (x+1, y),
            (x-1, y+1), (x, y+1), (x+1, y+1),
        ]
        for n in neighbors:
            if 0 <= n[0] < len(grid[0]) and 0 <= n[1] < len(grid) and n not in flashed:
                grid[n[1]][n[0]] += 1
                if grid[n[1]][n[0]] == 10:
                    flashing.add(n)
        flashed.add((x,y))
    
    for octo in flashed:
        grid[octo[1]][octo[0]] = 0
    
    return len(flashed)


def part_a(content):
    grid = []
    for row in content:
        grid.append(list(map(int, row)))

    count = 0
    for step in range(100):
        count += process_step(grid)
    
    return count


def part_b(content):
    grid = []
    for row in content:
        grid.append(list(map(int, row)))

    step = 0
    while True:
        step += 1
        if process_step(grid) == len(grid)*len(grid[0]):
            return step


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.splitlines())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
