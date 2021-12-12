from aocd import data


####################
# TEST DATA
####################
test_data = """\
3,4,3,1,2
"""
test_a_answer = "5934"
test_b_answer = "26984457539"


####################
# Puzzle solutions
####################
count_cache = {}
def recur_fish(days_till_popping: int, days_left : int) -> int:
    fish_count = 1
    if days_till_popping > days_left:
        return fish_count
    
    if (days_till_popping, days_left) in count_cache:
        return count_cache[(days_till_popping, days_left)]
    
    for i in range(days_left-days_till_popping, 0, -7):
        fish_count += recur_fish(9, i)
    
    count_cache[(days_till_popping, days_left)] = fish_count
    return fish_count


def part_a(content):
    fish = list(map(int, content))
    count = 0
    for f in fish:
        count += recur_fish(f, 80)
    return count


def part_b(content):
    fish = list(map(int, content))
    count = 0
    for f in fish:
        count += recur_fish(f, 256)
    return count


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data.split(',')

    test_a = part_a(test_data.split(','))
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    test_b = part_b(test_data.split(','))
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
