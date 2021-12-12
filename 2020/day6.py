from aocd import data


####################
# TEST DATA
####################
test_data = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""
test_a_answer = "11"
test_b_answer = "6"


####################
# Puzzle solutions
####################
def part_a(content):
    groups = [answers.replace('\n', '') for answers in content.split('\n\n')]
    count = 0
    for group in groups:
        count += len(set(group))
    return count


def part_b(content):
    groups = [answers.splitlines() for answers in content.split('\n\n')]
    count = 0
    for group in groups:
        answers = {}
        for person in group:
            for answer in person:
                answers[answer] = answers.get(answer, 0)+1
        
        count += len(list(filter(lambda x: x==len(group), answers.values())))
    return count


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
