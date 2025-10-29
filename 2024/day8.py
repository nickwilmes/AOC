from aocd import data
import itertools
from helpers import Grid, parse_grid, create_blank_grid, Position, copy_grid, inside_grid, get_velocity


####################
# TEST DATA
####################
test_data = """\
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
"""
test_b_data = test_data
test_a_answer = "14"
test_b_answer = "34"


####################
# Puzzle solutions
####################
def get_antennas(grid: Grid) -> list[Position]:
    antennas = {}
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            if char == '.':
                continue
            
            if char not in antennas:
                antennas[char] = []
            
            antennas[char].append((x, y))
    
    return antennas


def update_antinode_grid_a(antennas: list[Position], antinode_grid: Grid) -> Grid:
    new_grid = copy_grid(antinode_grid)
    antenna_combos = list(itertools.permutations(antennas, 2))
    for combo in antenna_combos:
        velocity = get_velocity(combo[0], combo[1])
        antinode = (combo[1][0] + velocity[0], combo[1][1] + velocity[1])
        if inside_grid(antinode, new_grid):
            new_grid[antinode[1]][antinode[0]] = '#'
    
    return new_grid


def update_antinode_grid_b(antennas: list[Position], antinode_grid: Grid) -> Grid:
    new_grid = copy_grid(antinode_grid)
    antenna_combos = list(itertools.permutations(antennas, 2))
    for combo in antenna_combos:
        velocity = get_velocity(combo[0], combo[1])
        antinode = (combo[1][0], combo[1][1])
        while inside_grid(antinode, new_grid):
            new_grid[antinode[1]][antinode[0]] = '#'
            antinode = (antinode[0] + velocity[0], antinode[1] + velocity[1])
    
    return new_grid


def count_char_in_grid(grid: Grid, char: str) -> int:
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == char:
                count += 1
    return count


def part_a(content):
    antenna_grid = parse_grid(content)
    antinode_grid = create_blank_grid(len(antenna_grid), len(antenna_grid[0]))
    
    antennas = get_antennas(antenna_grid)
    for frequency in antennas.keys():
        antinode_grid = update_antinode_grid_a(antennas[frequency], antinode_grid)
    
    ans = count_char_in_grid(antinode_grid, '#')
    return ans


def part_b(content):
    antenna_grid = parse_grid(content)
    antinode_grid = create_blank_grid(len(antenna_grid), len(antenna_grid[0]))
    
    antennas = get_antennas(antenna_grid)
    for frequency in antennas.keys():
        antinode_grid = update_antinode_grid_b(antennas[frequency], antinode_grid)
    
    ans = count_char_in_grid(antinode_grid, '#')
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
