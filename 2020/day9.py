from aocd import data


####################
# TEST DATA
####################
test_data = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576
"""
test_a_answer = "127"
test_b_answer = "62"


####################
# Puzzle solutions
####################
def part_a(content, preamble_length):
    content = list(map(int, content))
    for i, n in enumerate(content):
        if i<preamble_length:
            continue

        found = False
        for j in content[i-preamble_length:i]:
            if n-j in content[i-preamble_length:i]:
                found = True 
        
        if not found:
            return n



def part_b(content, preamble_length):
    goal = part_a(content, preamble_length)

    content = list(map(int, content))
    for i, n in enumerate(content):
        count = n
        j = 0
        while count < goal:
            j+=1
            count += content[i+j]
        if count == goal:
            nums = sorted(content[i:i+j+1])
            print(nums)
            return nums[0] + nums[-1]


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data.splitlines(), 5)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content, 25)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.splitlines(), 5)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content, 25)}")
    assert str(test_b) == test_b_answer
