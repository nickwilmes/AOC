from aocd import data


def part_a(content, target=2020):
    content = list(map(int, content))
    content.sort()
    i = 0
    j = len(content)-1
    while i < j:
        sum = content[i]+content[j]
        if sum == target:
            return content[i]*content[j]
        elif sum < target:
            i += 1
        else:
            j -= 1
    return -1


def part_b(content):
    content = list(map(int, content))
    content.sort()
    for j in reversed(range(len(content))):
        result = part_a(content[:j], 2020 - content[j])
        if result > 0:
            return result*content[j]
        j -= 1
    return None


test_data="""\
1721
979
366
299
675
1456
"""


if __name__ == "__main__":
    content = data.splitlines()
    assert str(part_a(test_data.splitlines())) == "514579"
    assert str(part_b(test_data.splitlines())) == "241861950"
    print(f"Part A answer: {part_a(content)}")
    print(f"Part B answer: {part_b(content)}")