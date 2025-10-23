from aocd import data
from collections import defaultdict
import math

####################
# TEST DATA
####################
test_data = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX"""

test_b_data = test_data
test_a_answer = "18"
test_b_answer = "9"


####################
# Puzzle solutions
####################
def horizontal(grid: list[str], word: str) -> int:
    count = 0
    for row in grid:
        count += row.count(word)
        count += row.count(word[::-1])  # Look for the reverse
    return count


def vertical(grid: list[str], word: str) -> int:
    # rotate grid 90 degrees
    g2 = rotate_90(grid)
    return horizontal(g2, word)


def uphill(grid: list[str], word: str) -> int:
    g2 = find_anti_diangle_lines(grid)
    return horizontal(g2, word)


def downhill(grid: list[str], word: str) -> int:
    g2 = find_diangle_lines(grid)
    return horizontal(g2, word)

def rotate_90(grid: list[str]) -> list[str]:
    g2 = ["".join(chars) for chars in list(zip(*grid))]
    return g2


def find_diangle_lines(grid: list[str]) -> list[str]:
    diagonals = {}
    rows = len(grid)
    cols = len(grid[0])

    for y in range(rows):
        for x in range(cols):
            diff = y-x
            c = grid[y][x]

            if diff not in diagonals:
                diagonals[diff] = []
            
            diagonals[diff].insert(0, c)
    
    new_grid = ["".join(diagonals[key]) for key in sorted(diagonals.keys())]

    return new_grid


def find_anti_diangle_lines(grid: list[str]) -> list[str]:
    diagonals = {}
    rows = len(grid)
    cols = len(grid[0])

    for y in range(rows):
        for x in range(cols):
            sum = y+x
            c = grid[y][x]

            if sum not in diagonals:
                diagonals[sum] = []
            
            diagonals[sum].insert(0, c)
    
    new_grid = ["".join(diagonals[key]) for key in sorted(diagonals.keys())]

    return new_grid


def part_a(grid: list[str]):
    directions = [horizontal, vertical, uphill, downhill]

    count = 0
    for direction in directions:
        count += direction(grid, "XMAS")
    
    return count


def is_valid_x_mas(grid: list[str], x: int, y: int) -> bool:
    tl, tr = grid[y-1][x-1], grid[y-1][x+1]
    bl, br = grid[y+1][x-1], grid[y+1][x+1]
    if tl == "M" and tr == "M" and bl == "S" and br == "S":
        return True
    if tl == "M" and tr == "S" and bl == "M" and br == "S":
        return True
    if tl == "S" and tr == "S" and bl == "M" and br == "M":
        return True
    if tl == "S" and tr == "M" and bl == "S" and br == "M":
        return True
    return False


def part_b(grid: list[str]):
    count = 0
    for y in range(1, len(grid)-1):  # No need to check first or last row
        for x in range(1, len(grid[y])-1):  # no need to check first or last column
            if grid[y][x] == 'A' and is_valid_x_mas(grid, x, y):
                count += 1

    return count




####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    # test_a = part_a(test_data.split())
    # print(f"Test A: {test_a}")
    # print(f"Part A answer: {part_a(content.split())}")
    # assert str(test_a) == test_a_answer

    test_b = part_b(test_b_data.split())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content.split())}")
    assert str(test_b) == test_b_answer