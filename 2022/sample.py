from aocd import data


####################
# TEST DATA
####################
test_data = """\
"""
test_a_answer = ""
test_b_answer = ""


####################
# Puzzle solutions
####################
def part_a(content):
    return None


def part_b(content):
    return None


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
