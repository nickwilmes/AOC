from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32"""
test_b_data = test_data
test_a_answer = "3"
test_b_answer = "14"


####################
# Puzzle solutions
####################
def part_a(content: str):
    ranges_raw, ids_raw = content.split('\n\n')
    
    ranges = []
    for range in ranges_raw.splitlines():
        min, _, max = range.partition('-')
        ranges.append((int(min), int(max)))
    
    ids = list(map(int, ids_raw.splitlines()))

    count = 0
    for id in tqdm(ids):
        for min, max in ranges:
            if min <= id and id <= max:
                count += 1
                break
    
    return count

def sort_mins(range: tuple[int, int]) -> int:
    return range[0]


def part_b(content: str):
    ranges_raw, _ = content.split('\n\n')
    
    ranges = []
    for r in ranges_raw.splitlines():
        low, _, high = r.partition('-')
        ranges.append((int(low), int(high)))
    
    sorted_ranges = sorted(ranges, key=sort_mins)

    i = 0
    while i < len(sorted_ranges)-1:
        r1, r2 = sorted_ranges[i], sorted_ranges[i+1]
        if r2[0] <= r1[1]:
            sorted_ranges[i] = (r1[0], max(r1[1], r2[1]))
            sorted_ranges.pop(i+1)
        else:
            i += 1

    return sum([r[1]-r[0]+1 for r in sorted_ranges])


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
