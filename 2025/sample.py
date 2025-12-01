from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
"""
test_b_data = test_data
test_a_answer = ""
test_b_answer = ""


####################
# Puzzle solutions
####################
def part_a(content: str):
    return None


def part_b(content: str):
    return None


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content)}")

    # test_b = part_b(test_b_data)
    # print(f"Test B: {test_b}")
    # assert str(test_b) == test_b_answer
    # print(f"Part B answer: {part_b(content)}")
