from typing import Optional
from aocd import data
from tqdm import tqdm
import helpers
from helpers import Grid, Position, UP, DOWN, LEFT, RIGHT


####
# WARNING: Part B is very slow.  implementing A* wouldprobably help a bunch
####

####################
# TEST DATA
####################
test_data = """\
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""
test_b_data = test_data
test_a_answer = "11048"
test_b_answer = "64"


####################
# Puzzle solutions
####################
Path = tuple[Position, str, int]

def part_a(content):
    grid = helpers.parse_grid(content)
    start = (0,0)
    finish = (0,0)
    for y in range(len(grid)):
        try:
            x = grid[y].index('S')
            start = (x, y)
        except ValueError:
            pass
        try:
            x = grid[y].index('E')
            finish = (x, y)
        except ValueError:
            pass

    pending: list[Path] = [(start, RIGHT, 0)]
    seen: dict[tuple[Position, str], int]= {}
    shortest_path: Optional[Path] = None

    while pending:
        pos, dir, cost = pending.pop()

        if grid[pos[1]][pos[0]] == '#':
            continue

        if (pos, dir) in seen:
            if cost < seen[(pos, dir)]:
                seen[(pos, dir)] = cost
            else:
                continue
        else:
            seen[(pos, dir)] = cost

        if pos == finish:
            if shortest_path is None or cost < shortest_path[2]:
                shortest_path = (pos, dir, cost)
            continue
        
        if shortest_path and cost >= shortest_path[2]:
            continue

        if dir == UP:
            pending.append((pos, LEFT, cost+1000))
            pending.append((pos, RIGHT, cost+1000))
            pending.append(((pos[0], pos[1]-1), dir, cost+1))

        elif dir == DOWN:
            pending.append((pos, LEFT, cost+1000))
            pending.append((pos, RIGHT, cost+1000))
            pending.append(((pos[0], pos[1]+1), dir, cost+1))

        elif dir == LEFT:
            pending.append((pos, UP, cost+1000))
            pending.append((pos, DOWN, cost+1000))
            pending.append(((pos[0]-1, pos[1]), dir, cost+1))

        elif dir == RIGHT:
            pending.append((pos, UP, cost+1000))
            pending.append((pos, DOWN, cost+1000))
            pending.append(((pos[0]+1, pos[1]), dir, cost+1))
    
    if shortest_path == None:
        raise Exception("No path to finish")

    return shortest_path[2]


Path2 = tuple[list[Position], str, int]


def part_b(content):
    grid = helpers.parse_grid(content)
    start = (0,0)
    finish = (0,0)
    for y in range(len(grid)):
        try:
            x = grid[y].index('S')
            start = (x, y)
        except ValueError:
            pass
        try:
            x = grid[y].index('E')
            finish = (x, y)
        except ValueError:
            pass

    pending: list[Path2] = [([start], RIGHT, 0)]
    seen: dict[tuple[Position, str], int]= {}
    shortest_paths: list[Path2] = []

    while pending:
        path, dir, cost = pending.pop()
        pos = path[-1]

        if grid[pos[1]][pos[0]] == '#':
            continue

        if (pos, dir) in seen:
            if cost <= seen[(pos, dir)]:
                seen[(pos, dir)] = cost
            else:
                continue
        else:
            seen[(pos, dir)] = cost

        if pos == finish:
            if not shortest_paths or cost < shortest_paths[0][2]:
                shortest_paths = [(path, dir, cost)]
            elif shortest_paths and cost == shortest_paths[0][2]:
                shortest_paths.append((path, dir, cost))
            continue
        
        if shortest_paths and cost >= shortest_paths[0][2]:
            continue

        if dir == UP:
            pending.append((path[:], LEFT, cost+1000))
            pending.append((path[:], RIGHT, cost+1000))
            new_path = path[:]
            new_path.append((pos[0], pos[1]-1))
            pending.append((new_path, dir, cost+1))

        elif dir == DOWN:
            pending.append((path[:], LEFT, cost+1000))
            pending.append((path[:], RIGHT, cost+1000))
            new_path = path[:]
            new_path.append((pos[0], pos[1]+1))
            pending.append((new_path, dir, cost+1))

        elif dir == LEFT:
            pending.append((path[:], UP, cost+1000))
            pending.append((path[:], DOWN, cost+1000))
            new_path = path[:]
            new_path.append((pos[0]-1, pos[1]))
            pending.append((new_path, dir, cost+1))

        elif dir == RIGHT:
            pending.append((path[:], UP, cost+1000))
            pending.append((path[:], DOWN, cost+1000))
            new_path = path[:]
            new_path.append((pos[0]+1, pos[1]))
            pending.append((new_path, dir, cost+1))
    
    if len(shortest_paths) == 0:
        raise Exception("No path to finish")

    points = []
    for s in shortest_paths:
        points.extend(s[0])
    
    return len(set(points))


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
