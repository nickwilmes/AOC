from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"""
test_b_data = test_data
test_a_answer = "1227775554"
test_b_answer = "4174379265"


####################
# Puzzle solutions
####################
def check_invalid_id_simple(id: int) -> bool:
    str_id = str(id)
    if len(str_id)%2 == 1:
        return False

    half_point = int(len(str_id)/2)
    a, b = str_id[:half_point], str_id[half_point:]
    if a==b:
        return True
    
    return False


def part_a(content: str):
    id_ranges = content.split(',')

    invalid_ids = []
    for id_range in tqdm(id_ranges):
        start, end = id_range.split('-')
        for id in range(int(start), int(end)+1):
            if check_invalid_id_simple(id):
                invalid_ids.append(id)
    
    return sum(invalid_ids)


def check_invalid_id_complex(id: int) -> bool:
    str_id = str(id)

    half_point = int(len(str_id)/2)
    for j in range(1, half_point+1):
        a, b = str_id[:j], str_id[-j:]
        if a==b and str_id.count(a)*j == len(str_id):
            return True
    
    return False


def part_b(content: str):
    id_ranges = content.split(',')

    invalid_ids = []
    for id_range in tqdm(id_ranges):
        start, end = id_range.split('-')
        for id in range(int(start), int(end)+1):
            if check_invalid_id_complex(id):
                invalid_ids.append(id)
    
    return sum(invalid_ids)


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
