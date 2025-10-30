from aocd import data
import helpers


####################
# TEST DATA
####################
test_data = """\
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
"""
test_b_data = test_data
test_a_answer = "36"
test_b_answer = "81"


####################
# Puzzle solutions
####################
def find_trailheads(grid: list[list[int]]) -> list[helpers.Position]:
    trailheads = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                trailheads.append((x, y))
    return trailheads


def get_all_paths(trailhead: helpers.Position, grid: list[list[int]]) -> list[list[helpers.Position]]:
    incomplete_paths = [[trailhead]]
    complete_paths = []
    while len(incomplete_paths) > 0:
        # breakpoint()
        path = incomplete_paths.pop()
        current_pos = path[-1]
        current_height = grid[current_pos[1]][current_pos[0]]
        left, right = (current_pos[0]-1, current_pos[1]), (current_pos[0]+1, current_pos[1])
        up, down = (current_pos[0], current_pos[1]-1), (current_pos[0], current_pos[1]+1)

        if current_height == 9:
            complete_paths.append(path)
            continue

        for pos in [left, right, up, down]:
            if helpers.inside_grid(pos, grid) and grid[pos[1]][pos[0]] == current_height+1:
                incomplete_paths.append([*path, pos])
    
    return complete_paths


def filter_paths_by_unique_dest(paths: list[list[helpers.Position]]) -> list[list[helpers.Position]]:
    new_paths = {}
    for path in paths:
        current_pos = path[-1]
        if current_pos not in new_paths:
            new_paths[current_pos] = []
        if len(path) >= len(new_paths[current_pos]):
            new_paths[current_pos] = path
    return new_paths


def part_a(content):
    s_grid = helpers.parse_grid(content)
    grid = []
    for row in s_grid:
        grid.append([int(x) for x in row])
    
    trailheads = find_trailheads(grid)
    ans = 0
    for trailhead in trailheads:
        paths = get_all_paths(trailhead, grid)
        paths = filter_paths_by_unique_dest(paths)
        ans += len(paths)
    
    return ans


def part_b(content):
    s_grid = helpers.parse_grid(content)
    grid = []
    for row in s_grid:
        grid.append([int(x) for x in row])
    
    trailheads = find_trailheads(grid)
    ans = 0
    for trailhead in trailheads:
        paths = get_all_paths(trailhead, grid)
        ans += len(paths)
    
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
