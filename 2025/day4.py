from aocd import data
from tqdm import tqdm
from helpers import Grid, parse_grid


####################
# TEST DATA
####################
test_data = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""
test_b_data = test_data
test_a_answer = "13"
test_b_answer = "43"


####################
# Puzzle solutions
####################

def inside_grid(grid: Grid, x: int, y: int) -> bool:
    return (x >= 0 and y >= 0 and y < len(grid) and x < len(grid[y]))


def get_neighboors(grid: Grid, x: int, y: int) -> list[tuple[int, int]]:
    neighboors = []
    # above
    if inside_grid(grid, x-1, y-1) and grid[y-1][x-1] == '@':
        neighboors.append((x-1, y-1))
    if inside_grid(grid, x, y-1) and grid[y-1][x] == '@':
        neighboors.append((x, y-1))
    if inside_grid(grid, x+1, y-1) and grid[y-1][x+1] == '@':
        neighboors.append((x+1, y-1))

    # same row
    if inside_grid(grid, x-1, y) and grid[y][x-1] == '@':
        neighboors.append((x-1, y))
    if inside_grid(grid, x+1, y) and grid[y][x+1] == '@':
        neighboors.append((x+1, y))

    # below
    if inside_grid(grid, x-1, y+1) and grid[y+1][x-1] == '@':
        neighboors.append((x-1, y+1))
    if inside_grid(grid, x, y+1) and grid[y+1][x] == '@':
        neighboors.append((x, y+1))
    if inside_grid(grid, x+1, y+1) and grid[y+1][x+1] == '@':
        neighboors.append((x+1, y+1))
    
    return neighboors


def part_a(content: str):
    grid: Grid = parse_grid(content)

    count = 0
    for y in tqdm(range(len(grid))):
        for x in range(len(grid[y])):
            if grid[y][x] != '@':
                continue
            
            neighboors = get_neighboors(grid, x, y)
            if len(neighboors) < 4:
                count += 1
    
    return count


def part_b(content: str):
    grid: Grid = parse_grid(content)

    total_count, count = 0, -1
    while count != 0:
        count = 0
        rolls_to_remove = []
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] != '@':
                    continue
                
                neighboors = get_neighboors(grid, x, y)
                if len(neighboors) < 4:
                    count += 1
                    rolls_to_remove.append((x, y))
        
        for roll in rolls_to_remove:
            x, y = roll
            grid[y][x] = '.'
        
        total_count += count
        print(f'Total (last step): {total_count} ({count})', end='\r')
    
    print()
    return total_count


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content)}")

    test_b = part_b(test_b_data)
    print(f"Test B: {test_b}")
    assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content)}")
