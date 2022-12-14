from aocd import data


####################
# TEST DATA
####################
test_data = """\
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
test_a_answer = "13"
test_b_answer = "140"


####################
# Puzzle solutions
####################
def compare(left, right, use_none = False):
    i = 0
    while len(left) > i:
        if len(right)-i == 0:
            return False

        if isinstance(left[i], int) and isinstance(right[i], int):
            if left[i] < right[i]:
                return True
            elif left[i] > right[i]:
                return False

        elif isinstance(left[i], list) and isinstance(right[i], int):
            comp = compare(left[i], [right[i]], True)
            if comp != None:
                return comp

        elif isinstance(left[i], int) and isinstance(right[i], list):
            comp = compare([left[i]], right[i], True)
            if comp != None:
                return comp
        
        if isinstance(left[i], list) and isinstance(right[i], list):
            comp = compare(left[i], right[i], True)
            if comp != None:
                return comp
    
        i += 1

    if len(right)-i > 0:
        return True
    elif use_none:
        return None
    else:
        return True


def part_a(content):
    ans = 0
    for i, lists in enumerate(content.split("\n\n")):
        left, right = lists.splitlines()
        left = eval(left)
        right = eval(right)
        comp = compare(left, right)
        if comp == True or comp == None:
            ans += i + 1
    
    return ans


def part_b(content):
    content = content.replace('\n\n', '\n')
    packets = content.splitlines()
    packets.append('[[2]]')
    packets.append('[[6]]')
    packets = [eval(p) for p in packets]

    # sort packets
    for h in reversed(range(len(packets))):
        for l in range(h):
            if compare(packets[l], packets[h]) == False:
                packets[l], packets[h] = packets[h], packets[l]

    index_2 = packets.index([[2]])
    index_6 = packets.index([[6]])
    return (index_2+1) * (index_6+1)


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
