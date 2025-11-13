import os


Grid = list[list[str]]
Position = tuple[int, int]


def parse_grid(input: str) -> Grid:
    grid = []
    for row in input.split():
        grid.append([c for c in row])
    return grid


def create_blank_grid(width: int, height: int, default_char: str = '.') -> Grid:
    grid = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(default_char)
        grid.append(row)
    return grid


def copy_grid(grid: Grid) -> Grid:
    return [r[:] for r in grid]


def inside_grid(pos: Position, grid: Grid) -> bool:
    x, y = pos
    return (x >= 0 and y >= 0 and y < len(grid) and x < len(grid[y]))


def get_velocity(start: Position, end: Position) -> tuple[int, int]:
    return (end[0]-start[0], end[1]-start[1])


def print_grid(grid: Grid) -> None:
    for row in grid:
        print(''.join(row))


def clear_screen():
    # Clears screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')

