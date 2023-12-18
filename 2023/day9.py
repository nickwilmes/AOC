from aocd import data


####################
# TEST DATA
####################
test_data = """\
0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

test_a_answer = "114"
test_b_answer = "2"


####################
# Puzzle solutions
####################


def find_next_value(history: list[int]) -> int:
    diffs = [history[i] - history[i - 1] for i in range(1, len(history))]
    if not all([x == 0 for x in diffs]):
        diffs.append(find_next_value(diffs))

    return history[-1] + diffs[-1]


def find_prev_value(history: list[int]) -> int:
    diffs = [history[i] - history[i - 1] for i in range(1, len(history))]
    if not all([x == 0 for x in diffs]):
        diffs.insert(0, find_prev_value(diffs))

    return history[0] - diffs[0]


def part_a(content: str):
    data = content.split("\n")

    answers = []
    for line in data:
        history = list(map(int, line.split()))
        answers.append(find_next_value(history))

    return sum(answers)


def part_b(content: str):
    data = content.split("\n")

    answers = []
    for line in data:
        history = list(map(int, line.split()))
        answers.append(find_prev_value(history))

    return sum(answers)


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
