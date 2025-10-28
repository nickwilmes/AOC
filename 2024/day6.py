from aocd import data


####################
# TEST DATA
####################
test_data = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""
test_b_data = test_data
test_a_answer = "41"
test_b_answer = "6"


Grid = list[list[str]]
UP, DOWN, LEFT, RIGHT = "^", "V", "<", ">"
DIRECTIONS = [UP, DOWN, LEFT, RIGHT]

class LoopException(Exception):
    pass


def parse_grid(input: str) -> Grid:
    grid = []
    for row in input.split():
        grid.append([c for c in row])
    return grid


def find_starting_location(grid: Grid) -> tuple[int, int]:
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] in DIRECTIONS:
                return x, y
    
    import pdb; pdb.set_trace()


def inside_grid(x: int, y: int, grid: Grid) -> bool:
    return (x >= 0 and y >= 0 and y < len(grid) and x < len(grid[y]))


def get_next_step(x: int, y: int, grid: Grid, memory: dict[tuple[int, int, str], bool]) -> tuple[int, int, str]:
    direction = grid[y][x]
    if (x, y, direction) in memory:
        raise LoopException()
    memory[(x, y, direction)] = True

    if direction == UP:
        if inside_grid(x, y-1, grid) and grid[y-1][x] == '#':
            grid[y][x] = RIGHT
            return get_next_step(x, y, grid, memory)
        else:
            return x, y-1, direction
    if direction == DOWN:
        if inside_grid(x, y+1, grid) and grid[y+1][x] == '#':
            grid[y][x] = LEFT
            return get_next_step(x, y, grid, memory)
        else:
            return x, y+1, direction
    if direction == LEFT:
        if inside_grid(x-1, y, grid) and grid[y][x-1] == '#':
            grid[y][x] = UP
            return get_next_step(x, y, grid, memory)
        else:
            return x-1, y, direction
    if direction == RIGHT:
        if inside_grid(x+1, y, grid) and grid[y][x+1] == '#':
            grid[y][x] = DOWN
            return get_next_step(x, y, grid, memory)
        else:
            return x+1, y, direction
    
    import pdb; pdb.set_trace()


def draw_path(grid: Grid) -> Grid:
    x, y = find_starting_location(grid)

    memory = {}
    new_grid = [r[:] for r in grid]
    while inside_grid(x, y, new_grid):
        new_x, new_y, new_direction = get_next_step(x, y, new_grid, memory)
        new_grid[y][x] = 'X'
        if inside_grid(new_x, new_y, new_grid):
            new_grid[new_y][new_x] = new_direction

        x, y = new_x, new_y
    
    return new_grid

####################
# Puzzle solutions
####################
def part_a(content):
    grid = parse_grid(content)

    drawn_grid = draw_path(grid)
    count = 0
    for row in drawn_grid:
        count += row.count("X")
    return count


def part_b(content):
    grid = parse_grid(content)

    drawn_grid = draw_path(grid)
    count = 0
    for y in range(len(drawn_grid)):
        for x in range(len(drawn_grid[y])): 
            if drawn_grid[y][x] == 'X' and grid[y][x] not in DIRECTIONS:
                test_grid = [r[:] for r in grid]
                test_grid[y][x] = '#'
                try:
                    draw_path(test_grid)
                except LoopException:
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

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
