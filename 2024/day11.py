from aocd import data
import functools


####################
# TEST DATA
####################
test_data = """\
125 17
"""
test_b_data = test_data
test_a_answer = "55312"
test_b_answer = "65601038650482"

MULTI_BLINK_CACHE = {}

####################
# Puzzle solutions
####################
def even_split(stone: int) -> list[str]:
    s_stone = str(stone)
    half = int(len(s_stone)/2)
    return [s_stone[:half], s_stone[half:]]


@functools.lru_cache()
def blink(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    
    if len(str(stone))%2 == 0:
        return [int(s) for s in even_split(stone)]

    return [stone*2024]


def multi_blink(input_stone: int, blinks: int) -> list[int]:
    if input_stone in MULTI_BLINK_CACHE:
        return MULTI_BLINK_CACHE[input_stone][:]

    stones = [input_stone]
    for _ in range(blinks):
        new_stones = []
        for stone in stones:
            new_stones.extend(blink(stone))
        stones = new_stones
    
    MULTI_BLINK_CACHE[input_stone] = stones[:]
    return MULTI_BLINK_CACHE[input_stone][:]


def part_a(content):
    stones = [int(s) for s in content.split(" ")]

    blinks = 5
    for n in range(0, 25, blinks):
        new_stones = []
        for stone in stones:
            new_stones.extend(multi_blink(stone, blinks))
        stones = new_stones
    
    return len(stones)


def dict_blink(input_stones: dict[int, int]) -> dict[int, int]:
    new_stones = {}
    for input_stone in input_stones.keys():
        update = blink(input_stone)
        for s in update:
            if s not in new_stones:
                new_stones[s] = 0
            new_stones[s] += input_stones[input_stone]
    return new_stones


def part_b(content):
    '''
    Realized that the order of the stones doesn't matter, so
    we only have to update each number once and then count how
    many times that number appears in the line
    '''
    stones = {int(s): 1 for s in content.split(" ")}

    for _ in range(75):
        stones = dict_blink(stones)
    
    return sum(stones.values())


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
