from aocd import data
from math import prod


####################
# TEST DATA
####################
test_data = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """
test_b_data = test_data
test_a_answer = "4277556"
test_b_answer = "3263827"


####################
# Puzzle solutions
####################
def part_a(content: str):
    problems = []

    first_line = content.splitlines()[0]
    last_line = content.splitlines()[-1]

    # setup the list of problems
    for num in first_line.split():
        problems.append([int(num)])
    
    # add the rest of the nums to the problems
    for line in content.splitlines()[1:-1]:
        for i, num in enumerate(line.split()):
            problems[i].append(int(num))

    # do the math
    answers = []
    for i, action in enumerate(last_line.split()):
        if action == '+':
            answers.append(sum(problems[i]))
        else:
            answers.append(prod(problems[i]))
    
    return sum(answers)


def part_b(content: str):
    # Set up list of problems
    problems = []
    for _ in range(len(content.splitlines()[-1].replace(' ',''))):
        problems.append([])
    problem_index = 0

    # parse the numbers from the lines
    nums: list[str] = []
    for i in range(max([len(l) for l in content.splitlines()])):
        digits = []
        for line in content.splitlines()[:-1]:
            if i<len(line):
                digits.append(line[i])
            else:
                digits.append('0')
        
        if all([d == ' ' for d in digits]):  # reached end of problem
            problems[problem_index].extend([int(n) for n in nums])
            problem_index += 1
            nums = []
        else:
            nums.append("".join(digits).replace(' ', ''))
    
    # add nums for the final problem
    problems[problem_index].extend([int(n) for n in nums])

    # do the math
    answers = []
    for i, action in enumerate(content.splitlines()[-1].split()):
        if action == '+':
            answers.append(sum(problems[i]))
        else:
            answers.append(prod(problems[i]))
    
    return sum(answers)
            
            


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
