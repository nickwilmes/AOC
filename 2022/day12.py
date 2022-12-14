from aocd import data
import networkx
import math


####################
# TEST DATA
####################
test_data = """\
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""
test_a_answer = "31"
test_b_answer = "29"


####################
# Puzzle solutions
####################


class Node:
    def __init__(self, parent, position, height):
        self.position = position
        self.parent = parent
        self.height = height

        self.g = 0
        self.h = 0
        self.f = 0
    

    def __eq__(self, other):
        return self.position == other.position


def astar(map):
    # Find start and end positions
    start_pos = None
    end_pos = None
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'S':
                start_pos = (x, y)
            if map[y][x] == 'E':
                end_pos = (x, y)

    start_node = Node(None, start_pos, 'a')
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end_pos, 'z')
    end_node.g = end_node.h = end_node.f = 0

    # init open andclosed lists
    open_list = [start_node]
    closed_list = []

    # Start processing the open list
    while len(open_list) > 0:

        # get shortest path node
        current_node = open_list[0]
        current_index = 0
        for i, node in enumerate(open_list):
            if node.f < current_node.f:
                current_index = i
                current_node = node

        # move current node to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # check if we found the end node
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        # create child nodes
        children = []
        for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            pos = (current_node.position[0] + direction[0], current_node.position[1] + direction[1])
            
            # make sure we are still on the map
            if pos[0] > (len(map[0])-1) or pos[0] < 0 or pos[1] > (len(map)-1) or pos[1] < 0:
                continue
            
            # make sure we can reach that spot
            height = map[pos[1]][pos[0]]
            if height == 'E':
                height = 'z'

            if ord(current_node.height) + 1 < ord(height):
                continue

            # create child
            children.append(Node(current_node, pos, height))
        
        # handle adding children to open list
        for child in children:

            # check if in closed list
            if child in closed_list:
                continue

            # create child values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2) + ((ord(child.height) - ord(end_node.height)) ** 2)
            child.f = child.g + child.h

            # only add to open list if there is not a faster way in the list
            found = False
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    found = True
                    break
            
            if not found:
                open_list.append(child)


def build_graph(map: list[list[str]]) -> networkx.DiGraph:
    graph = networkx.DiGraph()
    for y in range(len(map)):
        for x in range(len(map[y])):
            graph.add_node((x, y))
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx = x+d[0]
                ny = y+d[1]
                if nx < 0 or nx >= len(map[0]):
                    continue
                if ny < 0 or ny >= len(map):
                    continue
                # graph.add_edge((x, y), (nx, ny))
                if map[y][x] + 1 >= map[ny][nx]:
                    graph.add_edge((x, y), (nx, ny))
    
    return graph


def part_a(content):
    start = None
    end = None
    for y, line in enumerate(content.splitlines()):
        for x in range(len(line)):
            if line[x] == 'S':
                start = (x, y)
            elif line[x] == 'E':
                end = (x, y)
    
    map = []
    for row in content.splitlines():
        row = row.replace("S", "a")
        row = row.replace("E", "z")
        map.append([ord(x) for x in list(row)])
        
    graph = build_graph(map)
    path = networkx.shortest_path(graph, start, end)

    return len(path)-1


def part_b(content):
    low_points = []
    top = None
    for y, line in enumerate(content.splitlines()):
        for x in range(len(line)):
            if line[x] == 'S' or line[x] == 'a':
                low_points.append((x, y))
            elif line[x] == 'E':
                top = (x, y)
    
    map = []
    for row in content.splitlines():
        row = row.replace("S", "a")
        row = row.replace("E", "z")
        map.append([ord(x) for x in list(row)])
        
    graph = build_graph(map)
    shortest = math.inf
    for low_point in low_points:
        try:
            distance = networkx.shortest_path_length(graph, low_point, top)
        except networkx.NetworkXNoPath:
            continue
        if distance < shortest:
            shortest = distance

    return shortest


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
