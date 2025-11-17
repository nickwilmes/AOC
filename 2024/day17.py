from aocd import data
from tqdm import tqdm


####################
# TEST DATA
####################
test_data = """\
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0"""
test_b_data = """\
Register A: 2024
Register B: 0
Register C: 0

Program: 0,3,5,4,3,0"""
test_a_answer = "4,6,3,5,6,3,5,2,1,0"
test_b_answer = "117440"


####################
# Puzzle solutions
####################
Reg = tuple[int, int, int]

def get_combo(reg: Reg, operand: int) -> int:
    combo_operand_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg[0], 5: reg[1], 6: reg[2]}
    return combo_operand_map[operand]


def adv(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    a, b = reg[0], get_combo(reg, operand)
    reg = int(a/(2**b)), reg[1], reg[2]
    return reg, ptr+2, output


def bxl(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    # bitwise xor
    a, b = reg[1], operand
    reg = reg[0], a^b, reg[2]
    return reg, ptr+2, output


def bst(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    combo_operand_map = {0: 0, 1: 1, 2: 2, 3: 3, 4: reg[0], 5: reg[1], 6: reg[2]}
    a = get_combo(reg, operand)
    reg = reg[0], a%8, reg[2]
    return reg, ptr+2, output


def jnz(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    if reg[0] == 0:
        return reg, ptr+2, output
    return reg, operand, output


def bxc(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    a, b = reg[1], reg[2]
    reg = reg[0], a^b, reg[2]
    return reg, ptr+2, output


def out(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    a = get_combo(reg, operand)
    output.append(a%8)
    return reg, ptr+2, output


def bdv(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    a, b = reg[0], get_combo(reg, operand)
    reg = reg[0], int(a/(2**b)), reg[2]
    return reg, ptr+2, output
    

def cdv(reg: Reg, operand: int, ptr: int, output: list[int]) -> tuple[Reg, int, list[int]]:
    a, b = reg[0], get_combo(reg, operand)
    reg = reg[0], reg[1], int(a/(2**b))
    return reg, ptr+2, output
    

def part_a(content):
    reg_str, program_str = content.split("\n\n")
    reg: Reg = tuple([int(s.rpartition(' ')[-1]) for s in reg_str.split('\n')]) # type: ignore
    program = [int(i) for i in program_str.partition(' ')[-1].split(',')]

    instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}

    output = []
    ptr = 0
    while ptr < len(program):
        reg, ptr, output = instruction_map[program[ptr]](reg, program[ptr+1], ptr, output)

    return ','.join([str(i) for i in output])


def run_program(reg: Reg, program: list[int]) -> list[int]:
    instruction_map = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}
    output = []
    ptr = 0
    while ptr < len(program):
        reg, ptr, output = instruction_map[program[ptr]](reg, program[ptr+1], ptr, output)
    
    return output

def get_next_num(program: list[int], partial_ans: list[int]) -> list[int]:
    a=0
    for j in range(len(partial_ans)):
        a += partial_ans[j]*2**(3*(j+1))  # the j+1 is to make room for the test numbers below

    possible_nums = []
    for i in range(8):
        test_reg = a+i, 0, 0
        output = run_program(test_reg, program)
        if output == program[-(len(partial_ans)+1):]:
            possible_nums.append(i)
    
    return possible_nums


def part_b(content):
    reg_str, program_str = content.split("\n\n")
    reg: Reg = tuple([int(s.rpartition(' ')[-1]) for s in reg_str.split('\n')]) # type: ignore
    program = [int(i) for i in program_str.partition(' ')[-1].split(',')]

    lowest_working_a = float("INF")
    pending: list[list[int]] = [[]]
    while len(pending):
        partial = pending.pop()
        resp = get_next_num(program, partial)

        for ans in resp:
            nums = [ans, *partial]
            a=0
            for j in range(len(nums)):
                a += nums[j]*2**(3*(j))
            
            output = run_program((a, 0, 0), program)
            if output == program and a < lowest_working_a:
                lowest_working_a = a

            pending.append(nums)
        # breakpoint()
    
    return lowest_working_a


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
