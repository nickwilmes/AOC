import math
import time
from typing import Optional
from aocd import data


####################
# TEST DATA
####################
test_data = """\
498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
"""
test_a_answer = "24"
test_b_answer = "93"


####################
# Puzzle solutions
####################

SPAWN_POINT = (500, 0)

class SandOverflow(Exception):
    pass


def create_empty_grid(width: int, height: int) -> list[list[str]]:
    grid =[]
    for y in range(height+1):
        grid.append([])
        for x in range(width+1):
            grid[y].append('.')
    return grid


def draw(grid: list[list[str]], draw_start: Optional[tuple[int, int]] = None, draw_stop: Optional[tuple[int,int]] = None) -> None:
    if draw_start == None:
        draw_start = (0,0)
    if draw_stop == None:
        draw_stop = (len(grid[0]), len(grid))

    for row in grid[draw_start[1]:draw_stop[1]]:
        print(''.join(row[draw_start[0]:draw_stop[0]]))
    
    print('-----------------------')


def convert_wall_to_points(wall: list[tuple[int, int]]) -> list[tuple[int, int]]:
    points = []
    
    # right
    if wall[0][0] < wall[1][0]:
        for x in range(wall[0][0], wall[1][0]+1):
            points.append((x, wall[0][1]))
    
    # left
    if wall[0][0] > wall[1][0]:
        for x in range(wall[1][0], wall[0][0]+1):
            points.append((x, wall[0][1]))
    
    # up
    if wall[0][1] < wall[1][1]:
        for y in range(wall[0][1], wall[1][1]+1):
            points.append((wall[0][0], y))
    
    # down
    if wall[0][1] > wall[1][1]:
        for y in range(wall[1][1], wall[0][1]+1):
            points.append((wall[0][0], y))
    
    return points


def fill_in_walls(grid: list[list[str]], walls: list[tuple[int, int]]) -> list[list[str]]:
    for wall in walls:
        for point in convert_wall_to_points(wall):
            grid[point[1]][point[0]] = '#'

    return grid


def parse_walls_from_input(content: str) -> list[tuple[int, int]]:
    walls = []
    for line in content.splitlines():
        points = []
        for point in line.split(' -> '):
            x, y = point.split(',')
            points.append((int(x), int(y)))
        
        for i in range(len(points)-1):
            walls.append([points[i], points[i+1]])
    
    return walls


def find_borders(walls: list[tuple[int, int]]) -> tuple[tuple[int, int]]:
    min_x, max_x = math.inf, -math.inf
    min_y, max_y = math.inf, -math.inf
    for wall in walls:
        for point in wall:
            if point[0] < min_x:
                min_x = point[0]
            if point[0] > max_x:
                max_x = point[0]
            if point[1] < min_y:
                min_y = point[1]
            if point[1] > max_y:
                max_y = point[1]
    
    return (min_x, min_y), (max_x, max_y)


def update(grid: list[list[str]], falling_sand: list[tuple[int, int]]) -> None:
    for i in range(len(falling_sand)):
        sand = falling_sand[i]
        if sand[1]+1 >= len(grid):
            falling_sand.remove(sand)
            falling_sand.append((500,0))
            continue

        if grid[sand[1]+1][sand[0]] == '.':
            grid[sand[1]][sand[0]] = '.'
            sand = (sand[0], sand[1]+1)
            grid[sand[1]][sand[0]] = 'o'
            falling_sand[i] = sand
        
        elif grid[sand[1]+1][sand[0]-1] == '.':
            grid[sand[1]][sand[0]] = '.'
            sand = (sand[0]-1, sand[1]+1)
            grid[sand[1]][sand[0]] = 'o'
            falling_sand[i] = sand
        
        elif grid[sand[1]+1][sand[0]+1] == '.':
            grid[sand[1]][sand[0]] = '.'
            sand = (sand[0]+1, sand[1]+1)
            grid[sand[1]][sand[0]] = 'o'
            falling_sand[i] = sand
        
        else:
            if sand == (500,0):
                grid[sand[1]][sand[0]] = 'o'
                raise SandOverflow()
                
            falling_sand.remove(sand)
            falling_sand.append((500,0))


def part_a(content):
    walls = parse_walls_from_input(content)
    
    min, max = find_borders(walls)

    grid = create_empty_grid(max[0]*2, max[1]+2)
    
    grid = fill_in_walls(grid, walls)
    falling_sand = [(500, 0)]

    draw_start = (min[0]-3, 0)
    draw_stop = (max[0]+3, max[1]+3)
    # draw(grid, draw_start, draw_stop)


    while True:
        update(grid, falling_sand)
        # draw(grid, draw_start, draw_stop)
        # time.sleep(0.01)

        if falling_sand and falling_sand[0][1] > max[1]:
            break

    count_sand = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'o':
                count_sand += 1

    return count_sand - 1  # don't want to count the falling sand


def part_b(content):
    walls = parse_walls_from_input(content)
    
    min, max = find_borders(walls)

    grid = create_empty_grid(max[0]*2, max[1]+1)
    
    grid = fill_in_walls(grid, walls)
    falling_sand = [(500, 0)]

    draw_start = (min[0]-3, 0)
    draw_stop = (max[0]+3, max[1]+3)
    # draw(grid, draw_start, draw_stop)


    try:
        while True:
            update(grid, falling_sand)
            # draw(grid, draw_start, draw_stop)
            # time.sleep(0.01)

    except SandOverflow:
        pass

    count_sand = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'o':
                count_sand += 1

    return count_sand


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
