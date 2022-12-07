from aocd import data


####################
# TEST DATA
####################
test_data = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
test_a_answer = "7"
test_b_answer = "19"


####################
# Puzzle solutions
####################
def part_a(content):
    i = 4
    while i<len(content):
        if len(set(content[i-4:i])) != 4:
            i+=1
        else:
            print(content[i-3:i+1])
            return i


def part_b(content):
    i = 14
    while i<len(content):
        if len(set(content[i-14:i])) != 14:
            i+=1
        else:
            print(content[i-14:i])
            return i


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
