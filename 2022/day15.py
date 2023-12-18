from dataclasses import dataclass
from aocd import data
from collections import defaultdict


####################
# TEST DATA
####################
test_data = """\
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
test_a_answer = "26"
test_b_answer = ""


####################
# Puzzle solutions
####################

@dataclass
class Sensor:
    pos: tuple[int, int]
    beacon: tuple[int, int]
    range: int

    
def parse_sensors(content: str) -> list[Sensor]:
    sensors = []
    for line in content.splitlines():
        sensor_str, beacon_str = line.split(": ")
        sensor_x = int(sensor_str.partition("=")[-1].partition(',')[0])
        sensor_y = int(sensor_str.rpartition("=")[-1])
        beacon_x = int(beacon_str.partition("=")[-1].partition(',')[0])
        beacon_y = int(beacon_str.rpartition("=")[-1])
        range = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
        sensors.append(Sensor((sensor_x, sensor_y), (beacon_x, beacon_y), range))

    return sensors


def get_min_max(sensors: list[Sensor]) -> tuple[tuple[int, int], tuple[int, int]]:
    min_x = None
    min_y = None
    max_x = None
    max_y = None
    for sensor in sensors:
        local_max_x = sensor.pos[0] + sensor.range
        local_max_y = sensor.pos[1] + sensor.range
        local_min_x = sensor.pos[0] - sensor.range
        local_min_y = sensor.pos[1] - sensor.range
        if max_x is None or local_max_x > max_x:
            max_x = local_max_x
        if max_y is None or local_max_y > max_y:
            max_y = local_max_y
        if min_x is None or local_min_x < min_x:
            min_x = local_min_x
        if min_y is None or local_min_y < min_y:
            min_y = local_min_y
    
    return ((min_x, min_y), (max_x, max_y))


def generate_row(sensors: list[Sensor], row: int, min_x: int, max_x: int):
    r = defaultdict(lambda: '.')
    for x in range(-10, max_x+1):
        found = False
        for s in sensors:
            if abs(x-s.pos[0])+abs(row-s.pos[1]) <= s.range:
                found = True
                break
        if found:
            r[x] = '#'
        else:
            r[x] = '.'
    
    for s in sensors:
        if s.pos[1] == row:
            r[s.pos[0]] = 'S'
        if s.beacon[1] == row:
            r[s.beacon[0]] = 'B'
    
    return r


def generate_full_map(sensors: list[Sensor]) -> tuple[tuple[int, int], tuple[int, int], dict[int, dict[int, str]]]:
    min, max = get_min_max(sensors)

    graph = defaultdict(lambda: defaultdict(lambda: '.'))
    for y in range(min[1], max[1]):
        graph[y] = generate_row(sensors, y, min[0], max[0])
    
    return (min, max, graph)


def print_full_graph(graph: dict[dict[int, str]], min: tuple[int, int], max: tuple[int, int]) -> None:
    for y in range(min[1], max[1]):
        r = []
        for x in range(min[1], max[0]):
            r.append(graph[y][x])
        print('{:3}'.format(y) + ''.join(r))


def part_a(content, row_to_process):
    sensors = parse_sensors(content)

    min, max = get_min_max(sensors)
    row = generate_row(sensors, row_to_process, min[0], max[0])

    # min, max, graph = generate_full_map(sensors)
    # print_full_graph(graph, min, max)

    print('-----------')
    header = ""
    # for i in range(min[0], max[0]+1):
    #     header = header + f"{i}"[-1]
    # print(header)
    str_row = ''.join([row[x] for x in range(min[0], max[0])])
    # print(str_row)
    count = len(list(filter(lambda x: x == '#', str_row)))

    beacon_count = len(list(filter(lambda x: x == 'B', str_row)))
    sensor_count = len(list(filter(lambda x: x == 'S', str_row)))

    return count


def part_b(content):
    return None


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data, 10)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content, 2_000_000)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
