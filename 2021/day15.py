from typing import Generator, List, Optional, Tuple
import heapq

from aocd import data


####################
# TEST DATA
####################
test_data = """\
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""
test_a_answer = "40"
test_b_answer = "315"


####################
# Puzzle solutions
####################
def get_neighbors(pos : Tuple[int, int]) -> Generator[Tuple[int, int]]:
    x, y = pos
    yield (x-1, y)
    yield (x+1, y)
    yield (x, y-1)
    yield (x, y+1)


def part_a(content : List[str]) -> int:
    grid : dict[Tuple[int, int], int] = {}
    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            grid[(x, y)] = int(cost)
    
    end : Tuple[int, int]= max(grid)  # max compares x and then uses y as a tie-breaker

    cheapest_at : dict[Tuple[int, int], int]= {}

    options : List[Tuple[int, Tuple[int, int]]]= [(0, (0,0))]
    while options:
        cost, current_pos = heapq.heappop(options)

        if current_pos in cheapest_at and cost >= cheapest_at[current_pos]:
            continue

        cheapest_at[current_pos] = cost

        if current_pos == end:
            return cost
        
        for n in get_neighbors(current_pos):
            if n in grid:
                options.append((cost + grid[n], n))


def part_b(content: List[str]) -> int:
    grid : dict[Tuple[int, int], int] = {}
    width, height = len(content[0]), len(content)
    for y, line in enumerate(content):
        for x, cost in enumerate(line):
            for my in range(5):
                for mx in range(5):
                    m_cost = int(cost) + mx + my
                    if m_cost >=10:
                        m_cost -= 9
                    grid[(x+(width*mx), y+(height*my))] = m_cost
    
    for y in range(46):
        for x in range(46):
            if (x, y) not in grid:
                print(f"missing ({x}, {y})")
    
    end : Tuple[int, int]= max(grid)  # max compares x and then uses y as a tie-breaker

    cheapest_at : dict[Tuple[int, int], int]= {}

    options : List[Tuple[int, Tuple[int, int]]]= [(0, (0,0))]
    while options:
        cost, current_pos = heapq.heappop(options)

        if current_pos in cheapest_at and cost >= cheapest_at[current_pos]:
            continue

        cheapest_at[current_pos] = cost

        if current_pos == end:
            return cost
        
        for n in get_neighbors(current_pos):
            if n in grid:
                options.append((cost + grid[n], n))


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")

    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.splitlines())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
