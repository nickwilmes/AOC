from aocd import data
import time
from tqdm import tqdm
import helpers
from helpers import Position


####################
# TEST DATA
####################
test_data = """\
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
"""
test_b_data = test_data
test_a_answer = "10092"
test_b_answer = "9021"

OPERATIONS = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

####################
# Puzzle solutions
####################
def move_object(grid: helpers.Grid, pos: Position, vel: Position) -> helpers.Grid:
    new_pos = pos[0]+vel[0], pos[1]+vel[1]
    new_value = grid[new_pos[1]][new_pos[0]]
    if new_value == '.':
        new_grid = helpers.copy_grid(grid)
        new_grid[new_pos[1]][new_pos[0]] = grid[pos[1]][pos[0]]
        new_grid[pos[1]][pos[0]] = '.'
        return new_grid
    
    elif new_value == 'O':
        new_grid = move_object(grid, new_pos, vel)
        new_value = new_grid[new_pos[1]][new_pos[0]]
        if new_value == '.':
            return move_object(new_grid, pos, vel)
    
    elif new_value in '[]':
        if new_value == '[':
            p1, p2 = new_pos, (new_pos[0]+1, new_pos[1])
        else:
            p2, p1 = new_pos, (new_pos[0]-1, new_pos[1])

        if vel[0] == 0: # moving up/down
            new_grid = move_object(grid, p1, vel)
            new_grid = move_object(new_grid, p2, vel)
            new_p1_val, new_p2_val = new_grid[p1[1]][p1[0]], new_grid[p2[1]][p2[0]]
            if new_p1_val == '.' and new_p2_val == '.':
                return move_object(new_grid, pos, vel)
        
        elif vel[0] == -1:  # moving left
            new_grid = move_object(grid, p1, vel)
            new_p1_val = new_grid[p1[1]][p1[0]]
            if new_p1_val == '.':
                new_grid = move_object(new_grid, p2, vel)
                return move_object(new_grid, pos, vel)
        
        elif vel[0] == 1:  # moving right
            new_grid = move_object(grid, p2, vel)
            new_p2_val = new_grid[p2[1]][p2[0]]
            if new_p2_val == '.':
                new_grid = move_object(new_grid, p1, vel)
                return move_object(new_grid, pos, vel)

    return grid  # hit a wall


def update_grid(grid: helpers.Grid, operation: str) -> helpers.Grid:
    pos = (0, 0)
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == '@':
                pos = (x, y)
                break
    
    vel = OPERATIONS[operation]
    new_grid = move_object(grid, pos, vel)
    return new_grid


def get_crates(grid: helpers.Grid) -> list[int]:
    crates = []
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            value = grid[y][x]
            if value == 'O' or value == '[':
                crates.append(y*100+x)
    
    return crates
    
    
def part_a(content: str) -> int:
    grid_str, _, operations_str = content.partition('\n\n')
    grid = helpers.parse_grid(grid_str)
    operations_str = operations_str.replace('\n','')
    operations: list[str] = list(operations_str.strip())

    for op in tqdm(operations):
        grid = update_grid(grid, op)
    
    crates = get_crates(grid)

    return sum(crates)


def part_b(content):
    grid_str, _, operations_str = content.partition('\n\n')
    grid_str = grid_str.replace('#', '##').replace('O', '[]').replace('.', '..').replace('@', '@.')
    grid = helpers.parse_grid(grid_str)
    operations_str = operations_str.replace('\n','')
    operations: list[str] = list(operations_str.strip())

    for op in tqdm(operations):
        grid = update_grid(grid, op)

        # helpers.clear_screen()
        # helpers.print_grid(grid)
        # time.sleep(0.01)
    
    crates = get_crates(grid)

    return sum(crates)


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content)}")

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content)}")
