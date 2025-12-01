from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""
test_b_data = test_data
test_a_answer = "3"
test_b_answer = "6"


####################
# Puzzle solutions
####################
def part_a(content: str):
    n = 50
    max = 100

    count = 0
    for command in tqdm(content.splitlines()):
        amount = int(command.replace("L", "-").replace("R", ""))
        n = (n-amount)%max
        
        if n == 0:
            count += 1
    
    return count


def part_b(content: str):
    n = 50
    max = 100

    count = 0
    for command in tqdm(content.splitlines()):
        direction, amount = command[0], int(command[1:])

        # handle commands greater than 100
        count += int(amount/max)
        amount = amount%max

        # rotate dial
        if direction == "L":
            if n == 0:  # for the edge case where you land exactly on 0
                n =100
            n -= amount
        else:
            n += amount
        
        if n>=100 or n<=0:
            count += 1
            n = n%max

    return count


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content)}")

    test_b = part_b(test_b_data)
    print(f"Test B: {test_b}")
    assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content)}")
