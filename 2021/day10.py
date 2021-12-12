from aocd import data


####################
# TEST DATA
####################
test_data = """\
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""
test_a_answer = "26397"
test_b_answer = "288957"


####################
# Puzzle solutions
####################
ILLEGAL_SCORE = {')': 3, ']': 57, '}': 1197, '>': 25137}
INCOMPLETE_SCORE = {')': 1, ']': 2, '}': 3, '>': 4}
CLOSE_CHAR = {'(': ')', '{': '}', '[': ']', '<': '>'}

class CorruptedError(Exception):
    def __init__(self, unxepeced_char, message="Unxepected closing character"):
        self.unexpected_char = unxepeced_char


def find_missing_closing_chars(line: str) -> str:
    open_chunks = []
    for c in line:
        if c in "([{<":
            open_chunks.append(c)
        else:
            current_chunk = open_chunks.pop()
            if (c != CLOSE_CHAR[current_chunk]):
                raise CorruptedError(c)
    
    open_chunks.reverse()
    return list(map(lambda x: CLOSE_CHAR[x], open_chunks))


def part_a(content):
    score = 0
    for line in content:
        try:
            find_missing_closing_chars(line)
        except CorruptedError as e:
            score += ILLEGAL_SCORE[e.unexpected_char]
    
    return score


def part_b(content):
    scores = []
    for line in content:
        try:
            missing_chars = find_missing_closing_chars(line)
        except CorruptedError:
            continue

        line_score = 0
        for c in missing_chars:
            line_score = line_score * 5 + INCOMPLETE_SCORE[c]
        scores.append(line_score)
    
    return sorted(scores)[int(len(scores)/2)]


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
