from aocd import data
from dataclasses import dataclass

import pdb

####################
# TEST DATA
####################
test_data = """\
2333133121414131402
"""
test_b_data = test_data
test_a_answer = "1928"
test_b_answer = "2858"


####################
# Puzzle solutions
####################
def get_checksum(blocks: list[str]) -> int:
    ans = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            ans += i * int(blocks[i])
    
    return ans


def decompress(code: str) -> list[str]:
    blocks = []
    file_step = True
    id = 0
    for i in range(len(code)):
        num = int(code[i])
        if file_step:
            blocks.extend([str(id)]*num)
            id += 1
        else:
            blocks.extend(['.']*num)
        file_step = not file_step
    
    return blocks


def format_disk_a(blocks: list[str]) -> list[str]:
    new_blocks = blocks[:]
    i, j = 0, len(blocks)-1
    while i<j:
        if new_blocks[i] != '.':
            i += 1
            continue
        if new_blocks[j] == '.':
            j -= 1
            continue
        new_blocks[i], new_blocks[j] = new_blocks[j], new_blocks[i]
        i += 1
        j -= 1
    
    return new_blocks


def find_max_id(blocks: list[str]) -> str:
    for id in blocks[::-1]:
        if id != '.':
            return id


def format_disk_b(blocks: list[str]) -> list[str]:
    new_blocks = blocks[:]
    id = find_max_id(blocks)

    while int(id) > 0:
        pos = new_blocks.index(id)
        size = new_blocks[pos:].count(id)

        space = 0
        for i in range(pos):
            if new_blocks[i] == '.':
                space += 1
            else:
                space = 0
            
            if space == size:
                new_blocks[i-space+1:i+1], new_blocks[pos:pos+size] = new_blocks[pos:pos+size], new_blocks[i-space+1:i+1]
                break
        
        id = str(int(id)-1)

    return new_blocks


def part_a(content):
    content = content.strip()
    blocks = decompress(content)
    blocks = format_disk_a(blocks)
    return get_checksum(blocks)


def part_b(content):
    content = content.strip()
    blocks = decompress(content)
    blocks = format_disk_b(blocks)
    return get_checksum(blocks)


####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data)
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == test_a_answer

    # test_b = part_b(test_data)
    # print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer
