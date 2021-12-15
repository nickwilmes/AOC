from typing import List
from dataclasses import dataclass
from aocd import data


####################
# TEST DATA
####################
test_data = """\
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""
test_a_answer = "17"
test_b_answer = ""


####################
# Puzzle solutions
####################
def process_grid(points: str) -> List[List[str]]:
    grid = [[]]
    for line in points.split():
        split = line.split(",")
        x, y = int(split[0]), int(split[1])
        while len(grid) < y+1:
            grid.append([])
        
        for l in grid:
            while len(l) < x+1:
                l.append(False)
    
        grid[y][x] = True
    
    return grid


def fold(grid, line):
    split = line.split('=')
    direction, index = split[0], split[1]
    if direction == 'x':
        i = j = int(index)
        while i >= 0 and j < len(grid[0]):
            for y in range(len(grid)):
                grid[y][i] = grid[y][i] or grid[y][j]
                grid[y][j] = False
            i -= 1
            j += 1
        for y in range(len(grid)):
            while len(grid[y]) > 2*int(index):
                grid[y].pop()
    if direction == 'y':
        i = j = int(index)
        while i >= 0 and j < len(grid):
            for x in range(len(grid[0])):
                grid[i][x] = grid[i][x] or grid[j][x]
                grid[j][x] = False
            i -= 1
            j += 1
        while len(grid) > 2*int(index):
            grid.pop()
    return grid



def part_a(content):
    grid, commands = content.split('\n\n')
    grid = process_grid(grid)

    command = commands.split('\n')[0]
    grid = fold(grid, command.split()[-1])
    
    count = 0
    for line in grid:
        count += sum(list(filter(lambda x: x, line)))
    
    return count

def part_b(content):
    grid, commands = content.split('\n\n')
    grid = process_grid(grid)

    for command in commands.strip().split('\n'):
        grid = fold(grid, command.split()[-1])
    
    for line in grid:
        print(''.join(list(map(lambda x: '#' if x else ' ', line))))


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
    # assert str(test_b) == test_b_answer
