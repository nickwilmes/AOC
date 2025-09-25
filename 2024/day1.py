from aocd import data
from collections import defaultdict


####################
# TEST DATA
####################
test_data = """\
3   4
4   3
2   5
1   3
3   9
3   3"""

test_b_data = test_data
test_a_answer = "11"
test_b_answer = "31"


####################
# Puzzle solutions
####################


def part_a(content: str):
    lines = content.split("\n")
    l1 = []
    l2 = []
    for line in lines:
        nums = line.split("   ")
        l1.append(int(nums[0]))
        l2.append(int(nums[-1]))
    
    l1.sort()
    l2.sort()

    total_distance = 0
    for i in range(len(l1)):
        diff = l1[i]-l2[i]
        if diff < 0:
            diff *= -1
        total_distance += diff

    return total_distance


def part_b(content):
    lines = content.split("\n")
    l1 = []
    l2 = defaultdict(int)
    for line in lines:
        nums = line.split("   ")
        l1.append(int(nums[0]))
        l2[int(nums[-1])] += 1

    score = 0
    for n in l1:
        num_score = n * l2[n]
        score += num_score

    return score


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_b_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer