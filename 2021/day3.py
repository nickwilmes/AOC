from aocd import data


####################
# TEST DATA
####################
test_data = """\
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""
test_a_answer = str(int("10110", 2) * int("01001", 2))
test_b_answer = "230"


####################
# Puzzle solutions
####################
def part_a(content):
    gamma = ""
    epsilon = ""
    for col in range(len(content[0])):
        if sum(list(map(lambda x: int(x[col]), content))) < len(content) / 2:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"

    return int(gamma, 2) * int(epsilon, 2)


##TODO: FIX THIS!!
def part_b(content):
    oxy_list = content[:]
    co2_list = content[:]

    i = 0
    while len(oxy_list) > 2 and i < len(oxy_list[0]):
        if sum(list(map(lambda x: int(x[i]), oxy_list))) < len(oxy_list) / 2:
            oxy_list = list(filter(lambda x: x[i] == "0", oxy_list))
            i += 1
        else:
            oxy_list = list(filter(lambda x: x[i] == "1", oxy_list))
            i += 1

    oxy = list(filter(lambda x: x[i] == "1", oxy_list))[0]

    i = 0
    while len(co2_list) > 2 and i < len(co2_list[0]):
        if sum(list(map(lambda x: int(x[i]), co2_list))) < len(co2_list) / 2:
            co2_list = list(filter(lambda x: x[i] == "1", co2_list))
            i += 1
        else:
            co2_list = list(filter(lambda x: x[i] == "0", co2_list))
            i += 1

    co2 = list(filter(lambda x: x[i] == "0", co2_list))[0]

    return int(oxy, 2) * int(co2, 2)


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
