from typing import List
from aocd import data


####################
# TEST DATA
####################
test_data = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
test_a_answer = "CMZ"
test_b_answer = "MCD"


####################
# Puzzle solutions
####################

def convert_input_drawing(input) -> List[List[str]]:
    stacks = []
    rows = list(reversed(input.splitlines()))
    
    first_row = rows.pop(0)
    for i in range(1, len(first_row), 4):
        stacks.append([first_row[i]])
    
    for row in rows:
        for i in range(1, len(row), 4):
            if not row[i] == " ":
                stacks[i//4].append(row[i])
    
    return stacks


def process_actions_a(stacks: List[List[str]], actions: List[str]) -> List[List[str]]:
    for action in actions:
        action = action.split(" ")
        num, start, end = int(action[1]), int(action[3])-1, int(action[5])-1
        for _ in range(num):
            stacks[end].append(stacks[start].pop())
    
    return stacks


def part_a(content):
    stacks = convert_input_drawing(content.partition(" 1")[0])
    actions = list(filter(lambda line: "move" in line, content.splitlines()))
    finished_stacks = process_actions_a(stacks, actions)

    return "".join([stack[-1] for stack in finished_stacks])


def process_actions_b(stacks: List[List[str]], actions: List[str]) -> List[List[str]]:
    for action in actions:
        action = action.split(" ")
        num, start, end = int(action[1]), int(action[3])-1, int(action[5])-1
        tmp = []
        for _ in range(num):
            tmp.insert(0, stacks[start].pop())
        stacks[end].extend(tmp)
    
    return stacks


def part_b(content):
    stacks = convert_input_drawing(content.partition(" 1")[0])
    actions = list(filter(lambda line: "move" in line, content.splitlines()))
    finished_stacks = process_actions_b(stacks, actions)

    return "".join([stack[-1] for stack in finished_stacks])


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
