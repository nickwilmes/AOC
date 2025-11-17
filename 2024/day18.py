from aocd import data
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


####################
# TEST DATA
####################
test_data = """\
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""
test_b_data = test_data
test_a_answer = "22"
test_b_answer = "6,1"


####################
# Puzzle solutions
####################
def print_path(grid: Grid, path: list) -> None:
    path_matrix = []
    for y in range(grid.height):
        row = []
        for x in range(grid.width):
            if grid.node(x, y) in path:
                row.append('O')
            elif grid.node(x, y).walkable:
                row.append('.')
            else:
                row.append('#')
        path_matrix.append(row)
    
    print('\n'.join([''.join(r) for r in path_matrix]))
    

def part_a(content, width, height, wait_time):
    # create matrix
    matrix = []
    for _ in range(height):
        matrix.append([1]*width)

    # create grid
    grid = Grid(matrix=matrix)

    # update grid with points
    wait = 0
    for point in content.split('\n'):
        if wait >= wait_time:
            break

        p = point.split(',')
        x, y = int(p[0]), int(p[1])
        grid.node(x, y).walkable = False
        wait += 1

    # create start and end points
    start = grid.node(0,0)
    end = grid.node(width-1, height-1)

    # create finder
    finder = AStarFinder()

    # find the best path
    path, _ = finder.find_path(start, end, grid)

    # print path
    # print_path(grid, path)

    return len(path)-1  # don't want to count the start node


def part_b(content, width, height):
    # create matrix
    matrix = []
    for _ in range(height):
        matrix.append([1]*width)

    # create grid
    grid = Grid(matrix=matrix)

    # create start and end points
    start = grid.node(0,0)
    end = grid.node(width-1, height-1)

    # create finder
    finder = AStarFinder()

    # update grid with the first 1024 points for real input (skip for test input)
    points = [(p.partition(',')[0], p.partition(',')[-1]) for p in content.split('\n')]
    if len(points) > 1024:
        for i in range(1024):
            p = points.pop(0)
            x, y = int(p[0]), int(p[1])
            grid.node(x,y).walkable = False

    # continue adding walls until there's no path left
    for i, point in enumerate(points):
        print(f"testing with {i+1024:06d} bits fallen", end='\r', flush=True)
        x, y = int(point[0]), int(point[1])
        grid.node(x,y).walkable = False

        path, _ = finder.find_path(start, end, grid)
        if len(path) == 0:
            print()
            return f'{x},{y}'


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data, 7, 7, 12)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content, 71, 71, 1024)}")

    test_b = part_b(test_b_data, 7, 7)
    print(f"Test B: {test_b}")
    assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content, 71, 71)}")
