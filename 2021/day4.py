from typing import List
from aocd import data


####################
# TEST DATA
####################
test_data = """\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
test_a_answer = "4512"
test_b_answer = "1924"


####################
# Puzzle solutions
####################
def read_board(lines: List[str]) -> List[List[int]]:
    ans = []
    for line in lines:
        ans.append(line.split())
    return ans


def cal_score(board: List[List[int]], number: int) -> int:
    ans = 0
    for row in board:
        for num in row:
            if num != "x":
                ans += int(num)
    return ans * number


def part_b(content):
    picks = list(map(int, content[0].split(",")))

    boards = []
    i = 1
    while i < len(content):
        if content[i] == "":
            i += 1
        else:
            boards.append(read_board(content[i : i + 5]))
            i += 5

    found = False
    winning_boards = []
    for pick in picks:
        for board in boards:
            for row in board:
                for i in range(5):
                    if row[i] == str(pick):
                        row[i] = "x"
                        found = True
                        if (
                            all(v == "x" for v in row)
                            or all(row[i] == "x" for row in board)
                        ) and board not in winning_boards:
                            winning_boards.append(board)
                        break
                if found:
                    found = False
                    break
        if len(winning_boards) == len(boards):
            return cal_score(winning_boards[-1], pick)
    raise Exception("Not all boards solved")


def part_a(content):
    picks = list(map(int, content[0].split(",")))

    boards = []
    i = 1
    while i < len(content):
        if content[i] == "":
            i += 1
        else:
            boards.append(read_board(content[i : i + 5]))
            i += 5

    found = False
    for pick in picks:
        for board in boards:
            for row in board:
                for i in range(5):
                    if row[i] == str(pick):
                        row[i] = "x"
                        found = True
                        if all(v == "x" for v in row) or all(
                            row[i] == "x" for row in board
                        ):
                            return cal_score(board, pick)
                        break
                if found:
                    found = False
                    break


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
