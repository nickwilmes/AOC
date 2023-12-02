from aocd import data
from functools import reduce


####################
# TEST DATA
####################
test_data = """\
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

test_a_answer = "8"
test_b_answer = "2286"


####################
# Puzzle solutions
####################


def part_a(content: str):
    lines = content.split("\n")

    limits = {"red": 12, "green": 13, "blue": 14}
    possible_games = []

    for line in lines:
        possible = True
        id, _, draws = line.partition(": ")
        id = id.rpartition(" ")[-1]
        draws = draws.split("; ")

        for draw in draws:
            colors = draw.split(", ")
            for color in colors:
                count, _, color_name = color.partition(" ")
                if int(count) > limits[color_name]:
                    possible = False
                    break
            if not possible:
                break

        if possible:
            possible_games.append(int(id))

    return sum(possible_games)


def part_b(content):
    lines = content.split("\n")

    games = []

    for line in lines:
        min_limits = {"red": 0, "green": 0, "blue": 0}
        id, _, draws = line.partition(": ")
        id = id.rpartition(" ")[-1]
        draws = draws.split("; ")

        for draw in draws:
            colors = draw.split(", ")
            for color in colors:
                count, _, color_name = color.partition(" ")
                if int(count) > min_limits[color_name]:
                    min_limits[color_name] = int(count)

        games.append(reduce((lambda x, y: x * y), min_limits.values()))

    return sum(games)


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
