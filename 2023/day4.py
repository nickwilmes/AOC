from aocd import data


####################
# TEST DATA
####################
test_data = """\
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

test_a_answer = "13"
test_b_answer = "30"


####################
# Puzzle solutions
####################


def get_num_matches(line: str) -> int:
    nums = line.partition(":")[-1]
    winning_nums, _, your_nums = nums.partition(" | ")
    winning_nums = winning_nums.split()
    your_nums = your_nums.split()

    matches = 0
    for num in winning_nums:
        if num in your_nums:
            matches += 1

    return matches


def part_a(content: str):
    lines = content.split("\n")
    scores = []

    for line in lines:
        matches = get_num_matches(line)

        if matches == 0:
            scores.append(0)
        else:
            scores.append(2 ** (matches - 1))

    return sum(scores)


def part_b(content):
    lines = content.split("\n")
    copies = [1] * len(lines)

    for i in range(len(lines)):
        matches = get_num_matches(lines[i])

        for c in range(i + 1, i + matches + 1):
            copies[c] = copies[c] + copies[i]

    return sum(copies)


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
