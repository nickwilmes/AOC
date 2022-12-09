from dataclasses import dataclass
from aocd import data


####################
# TEST DATA
####################
test_data = """\
30373
25512
65332
33549
35390
"""
test_a_answer = "21"
test_b_answer = "8"


####################
# Puzzle solutions
####################
@dataclass
class Tree:
    visible: bool = False
    height: int = 0
    score: int = 0


UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4


def convert_input_to_trees(content: str) -> list[list[Tree]]:
    ans = []
    for row in content.splitlines():
        tree_row = []
        for tree in row:
            tree_row.append(Tree(height=int(tree)))
        ans.append(tree_row)
    return ans


def check_dir(forest: list[list[Tree]], dir: int) -> None:
    if dir == LEFT:
        for r in range(len(forest)):
            tallest = -1
            for c in range(len(forest[0])):
                if forest[r][c].height > tallest:
                    forest[r][c].visible = True
                    tallest = forest[r][c].height
    elif dir == RIGHT:
        for r in range(len(forest)):
            tallest = -1
            for c in reversed(range(len(forest[0]))):
                if forest[r][c].height > tallest:
                    forest[r][c].visible = True
                    tallest = forest[r][c].height
    if dir == DOWN:
        for c in range(len(forest[0])):
            tallest = -1
            for r in range(len(forest)):
                if forest[r][c].height > tallest:
                    forest[r][c].visible = True
                    tallest = forest[r][c].height
    if dir == DOWN:
        for c in range(len(forest[0])):
            tallest = -1
            for r in reversed(range(len(forest))):
                if forest[r][c].height > tallest:
                    forest[r][c].visible = True
                    tallest = forest[r][c].height
    

def part_a(content):
    forest = convert_input_to_trees(content)
    check_dir(forest, LEFT)
    check_dir(forest, RIGHT)
    check_dir(forest, UP)
    check_dir(forest, DOWN)

    ans = 0
    for row in forest:
        ans += len(list(filter(lambda t: t.visible, row)))

    return ans
    

def get_score(forest: list[list[Tree]], pos: tuple[int, int]) -> int:
    return 0


def part_b(content):
    high_score = 0
    forest = convert_input_to_trees(content)
    for r in range(1, len(forest)-1):
        for c in range(1, len(forest[1])-1):
            score = get_score(forest, (c, r))
            if score > high_score:
                high_score = score

    return high_score

    ans = 0
    for row in forest:
        ans += len(list(filter(lambda t: t.visible, row)))

    return ans


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
