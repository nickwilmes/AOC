from aocd import data


####################
# TEST DATA
####################
test_data = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""
test_a_answer = "5"
test_b_answer = "8"


####################
# Puzzle solutions
####################
class CorruptedError(Exception):
    def __init__(self, acc, message="Infinite loop detected"):
        self.accumulator = acc


def run_boot(content):
    accumulator = i = 0
    processed_lines = set()
    while i < len(content):
        if i in processed_lines:
            raise CorruptedError(accumulator)
        processed_lines.add(i)

        command, amount = content[i].split()
        if command == 'nop':
            i += 1
            continue

        if amount[0] == '+':
            amount = int(amount[1:])
        else:
            amount = int(amount[1:]) * -1

        if command == 'jmp':
            i += amount
        elif command == 'acc':
            accumulator += amount
            i += 1
    return accumulator


def part_a(content):
    try:
        run_boot(content)
    except CorruptedError as e:
        return e.accumulator


def part_b(content):
    for i in range(len(content)):
        if content[i].startswith("acc"):
            continue

        if content[i].startswith("nop"):
            content[i] = content[i].replace("nop", "jmp")
        elif content[i].startswith("jmp"):
            content[i] = content[i].replace("jmp", "nop")
        
        try:
            return run_boot(content)
        except CorruptedError:
            if content[i].startswith("nop"):
                content[i] = content[i].replace("nop", "jmp")
            elif content[i].startswith("jmp"):
                content[i] = content[i].replace("jmp", "nop")





####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.splitlines())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
