from aocd import data


####################
# TEST DATA
####################
test_data = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
test_a_answer = "2"
test_b_answer = "4"


####################
# Puzzle solutions
####################
def part_a(content):
    count = 0
    for pair in content.splitlines():
        elves = pair.split(",")
        elves = [elf.split('-') for elf in elves]
        if int(elves[0][0]) >= int(elves[1][0]) and int(elves[0][1]) <= int(elves[1][1]):
            count += 1
        elif int(elves[1][0]) >= int(elves[0][0]) and int(elves[1][1]) <= int(elves[0][1]):
            count += 1

    return count


def part_b(content):
    count = 0
    for pair in content.splitlines():
        elves = pair.split(",")
        elves = [elf.split('-') for elf in elves]
        if int(elves[0][0]) >= int(elves[1][0]) and int(elves[0][0]) <= int(elves[1][1]):
            count += 1
        elif int(elves[1][0]) >= int(elves[0][0]) and int(elves[1][0]) <= int(elves[0][1]):
            count += 1

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
