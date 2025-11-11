from aocd import data
import helpers

####################
# TEST DATA
####################
test_data = """\
RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE
"""
test_b_data = test_data
test_a_answer = "1930"
test_b_answer = "1206"

PROCESSED_CELL = "?"
PROCESSED_PLOT = "#"

####################
# Puzzle solutions
####################
def extract_plot(starting_pos: helpers.Position, grid: helpers.Grid) -> tuple[list[helpers.Position], helpers.Grid]:
    tiles = []
    plant_type = grid[starting_pos[1]][starting_pos[0]]
    positions = [starting_pos]
    new_grid = helpers.copy_grid(grid)

    while len(positions) > 0:
        pos = positions.pop()
        value = new_grid[pos[1]][pos[0]]
        if value == PROCESSED_CELL:
            continue

        if value == plant_type:
            new_grid[pos[1]][pos[0]] = PROCESSED_CELL
            tiles.append(pos)

            up, down = (pos[0], pos[1]-1), (pos[0], pos[1]+1)
            left, right = (pos[0]-1, pos[1]), (pos[0]+1, pos[1])
            for n in [up, down, left, right]:
                if helpers.inside_grid(n, grid):
                    positions.append(n)
    
    for y in range(len(new_grid)):
        for x in range(len(new_grid[y])):
            if new_grid[y][x] == PROCESSED_CELL:
                new_grid[y][x] = PROCESSED_PLOT

    return tiles, new_grid


def calculate_cost_a(plot: list[helpers.Position]) -> int:
    parameter = 0
    area = len(plot)

    for pos in plot:
        up, down = (pos[0], pos[1]-1), (pos[0], pos[1]+1)
        left, right = (pos[0]-1, pos[1]), (pos[0]+1, pos[1])
        for n in [up, down, left, right]:
            if n not in plot:
                parameter += 1
    
    return area*parameter


def calculate_cost_b(plot: list[helpers.Position]) -> int:
    corners = 0
    area = len(plot)

    # special cases
    if area == 0:
        return 0
    if area == 1:
        return 4
    
    # get bounds
    min_x, max_x = plot[0][0], plot[0][0]
    min_y, max_y = plot[0][1], plot[0][1]
    for x, y in plot:
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
    
    # check 2x2 blocks for corners
    for y in range(min_y-1, max_y+1):
        for x in range(min_x-1, max_x+1):
            blocks = [(x,y),(x+1,y), (x,y+1), (x+1,y+1)]
            results = [int(pos in plot) for pos in blocks]
            one_corner_patterns = [[1, 0, 0, 0],
                                  [0, 1, 0, 0],
                                  [0, 0, 1, 0],
                                  [0, 0, 0, 1],
                                  [1, 1, 1, 0],
                                  [1, 1, 0, 1],
                                  [1, 0, 1, 1],
                                  [0, 1, 1, 1]]
            two_corner_patterns = [[1, 0, 0, 1],
                                  [0, 1, 1, 0]]
            if results in one_corner_patterns:
                corners += 1
            elif results in two_corner_patterns:
                corners += 2

    return area*corners


def part_a(content):
    grid = helpers.parse_grid(content)
    plots = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            plant = grid[y][x]
            if plant == '#':
                continue

            tiles, grid = extract_plot((x, y), grid)
            plots.append(tiles)
    
    return sum([calculate_cost_a(plot) for plot in plots])


def part_b(content):
    grid = helpers.parse_grid(content)
    plots = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            plant = grid[y][x]
            if plant == '#':
                continue

            tiles, grid = extract_plot((x, y), grid)
            plots.append(tiles)
    
    return sum([calculate_cost_a(plot) for plot in plots])


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
