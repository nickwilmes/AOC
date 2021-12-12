from aocd import data


####################
# TEST DATA
####################
test_data = """\
199
200
208
210
200
207
240
269
260
263
"""
test_a_answer = "7"
test_b_answer = "5"


####################
# Puzzle solutions
####################
def part_a(content):
    content = list(map(int, content))
    count = 0
    for i in range(1, len(content)):
        if content[i] > content[i - 1]:
            count += 1
    return count


def part_b(content):
    content = list(map(int, content))
    count = 0
    for i in range(3, len(content)):
        if content[i] > content[i - 3]:
            count += 1
    return count


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content)}")

    test_b = part_b(test_data.splitlines())
    print(f"Test B: {test_b}")
    assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content)}")
