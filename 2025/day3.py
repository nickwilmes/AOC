from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
987654321111111
811111111111119
234234234234278
818181911112111"""
test_b_data = test_data
test_a_answer = "357"
test_b_answer = "3121910778619"


####################
# Puzzle solutions
####################
def part_a(content: str):
    jolts = []
    for bank in tqdm(content.splitlines()):
        a, b, index = '0', '0', 0
        for i, c in enumerate(bank[:-1]):
            if c > a:
                a, index = c, i
        for c in bank[index+1:]:
            if c > b:
                b = c
        jolts.append(int(a+b))
    
    return sum(jolts)


def get_highest_jolt(num: str, size: int) -> str:
    a, index = '0', 0
    # breakpoint()
    for i, c in enumerate(num[:len(num)-size+1]):
        if c > a:
            a, index = c, i
    
    if size == 1:
        return a

    return a+get_highest_jolt(num[index+1:], size-1)


def part_b(content: str):
    jolts = []
    for bank in tqdm(content.splitlines()):
        jolts.append(int(get_highest_jolt(bank, 12)))
    
    return sum(jolts)


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
