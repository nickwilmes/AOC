from aocd import data


####################
# TEST DATA
####################
test_data = """\
addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
test_a_answer = "13140"
test_b_answer = """\
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""


####################
# Puzzle solutions
####################

CHECKPOINTS = [20, 60, 100, 140, 180, 220]


def part_a(content):
    cycle = 1
    x = 1
    signal_strengths = []
    for command in content.splitlines():
        if cycle in CHECKPOINTS:
            signal_strengths.append(x*cycle)
        elif command.startswith('addx') and cycle+1 in CHECKPOINTS:
            signal_strengths.append(x*(cycle+1))


        if command.startswith('addx'):
            amount = int(command.split()[-1])
            x += amount
            cycle += 2
        else:
            cycle += 1
    
    return sum(signal_strengths)


def draw(cycle: int, x: int) -> str:
    if abs(cycle - x) <= 1:
        return '#'
    return '.'


def part_b(content):
    cycle = 1
    x = 1
    output = []
    for command in content.splitlines():
        output.append(draw(cycle-1, x))
        if command.startswith('addx'):
            cycle = cycle % 40 + 1
            output.append(draw(cycle-1, x))
            amount = int(command.split()[-1])
            x += amount
            cycle = cycle % 40 + 1
        else:
            cycle = cycle % 40 + 1
    
    
    final_output = ""
    for r in [output[i:i + 40] for i in range(0, len(output), 40)]:
        final_output += f"{''.join(r)}\n"

    return final_output


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
    print(f"Test B:")
    print(f"{test_b}")
    print(f"Part B answer:")
    print(f"{part_b(content)}")
    assert test_b == test_b_answer
