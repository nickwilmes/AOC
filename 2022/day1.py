from aocd import data


####################
# TEST DATA
####################
test_data = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
test_a_answer = "24000"
test_b_answer = "45000"


####################
# Puzzle solutions
####################
def part_a(content):
    elves = content.split("\n\n")
    max_load = 0
    
    for elf in elves:
        items = elf.split("\n")
        items = [0 if i=='' else int(i) for i in items]
        load = sum(items)
        if load >= max_load:
            max_load = load
    
    return max_load


def part_b(content):
    elves = content.split("\n\n")
    loads = []
    
    for elf in elves:
        items = elf.split("\n")
        items = [0 if i=='' else int(i) for i in items]
        loads.append(sum(items))
    
    loads.sort(reverse=True)
    return sum(loads[0:3])


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
