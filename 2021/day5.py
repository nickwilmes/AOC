from typing import List
from aocd import data
from pprint import pprint
from collections import Counter


####################
# TEST DATA
####################
test_data = """\
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""
test_a_answer = "5"
test_b_answer = "12"


####################
# Puzzle solutions
####################
def part_a(content):
    hits = []
    for vent in content:
        start, end = vent.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                hits.append((i, x1))
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                hits.append((y1, i))
    hit_counts = Counter(hits).most_common()
    multiple_hits = list(filter(lambda x: x[1]>1, hit_counts))
    return len(multiple_hits)


def part_b(content):
    hits = []
    for vent in content:
        start, end = vent.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for i in range(y1, y2+1):
                hits.append((i, x1))
        elif y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for i in range(x1, x2+1):
                hits.append((y1, i))
        else:
            x, y = x1, y1
            while x != x2 and y!= y2:
                hits.append((y, x))
                if x < x2:
                    x += 1
                else:
                    x -= 1
                if y < y2:
                    y += 1
                else:
                    y -= 1
            hits.append((y2, x2))
    hit_counts = Counter(hits).most_common()
    multiple_hits = list(filter(lambda x: x[1]>1, hit_counts))
    return len(multiple_hits)


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
    print(f"Part B answer: {part_b(content)}") # 22308 too low, 22349 too high
    assert str(test_b) == test_b_answer
