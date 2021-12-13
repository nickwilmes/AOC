from typing import List
from aocd import data
from dataclasses import dataclass


####################
# TEST DATA
####################
test_data = """\
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""
test_a_answer = "10"
test_b_answer = "36"


####################
# Puzzle solutions
####################
def part_a(content):
    caves = {}
    for line in content:
        c1, c2 = line.split('-')
        caves.setdefault(c1, [])
        caves.setdefault(c2, [])
        caves[c1].append(c2)
        caves[c2].append(c1)
    
    incomplete_paths = []
    for cave in caves['start']:
        incomplete_paths.append(['start',cave])
    
    complete_paths = []
    while len(incomplete_paths) > 0:
        path = incomplete_paths.pop()
        for cave in caves[path[-1]]:
            if (
                cave.isupper() or
                (cave.islower() and cave not in path)
            ):
                if cave == 'end':
                    complete_paths.append(path[:]+[cave])
                else:
                    incomplete_paths.append(path[:]+[cave])

    return len(complete_paths)

@dataclass
class Path():
    caves: List[str]
    visited_small_cave_twice: bool = False

    
def part_b(content):
    caves = {}
    for line in content:
        c1, c2 = line.split('-')
        caves.setdefault(c1, [])
        caves.setdefault(c2, [])
        caves[c1].append(c2)
        caves[c2].append(c1)
    
    incomplete_paths : List[Path] = []
    for cave in caves['start']:
        incomplete_paths.append(Path(['start',cave]))
    
    complete_paths : List[Path]= []
    while len(incomplete_paths) > 0:
        path = incomplete_paths.pop()
        for cave in caves[path.caves[-1]]:
            if path.caves == ['start','b', 'A', 'c', 'A'] and cave == 'b':
                print()
            if cave.isupper():
                incomplete_paths.append(Path(path.caves[:]+[cave], path.visited_small_cave_twice))
            elif cave != "start":
                if not path.visited_small_cave_twice:
                    if cave == 'end':
                        complete_paths.append(Path(path.caves[:]+[cave]))
                    else:
                        incomplete_paths.append(Path(path.caves[:]+[cave], (cave in path.caves)))
                elif cave not in path.caves:
                    if cave == 'end':
                        complete_paths.append(Path(path.caves[:]+[cave]))
                    else:
                        incomplete_paths.append(Path(path.caves[:]+[cave], True))

    return len(complete_paths)


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
