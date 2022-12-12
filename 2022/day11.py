from dataclasses import dataclass
import math
from typing import Callable
from aocd import data


####################
# TEST DATA
####################
test_data = """\
Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
"""
test_a_answer = "10605"
test_b_answer = "2713310158"


####################
# Puzzle solutions
####################


@dataclass
class Monkey:
    items: list[int]
    operation: str
    divisor: int
    positive: int
    negitive: int
    inspections: int = 0
    lcd: int = 0

    def run_operation(self, item: int) -> int:
        new = eval(self.operation, {}, {"old": item})
        return int(new)
    
    def get_target(self, n: int) -> int:
        target = self.positive if int(n)%self.divisor == 0 else self.negitive
        return target

    def __lt__(self, other):
         return self.inspections < other.inspections


def input_to_data_objects(content: str) -> list[Monkey]:
    monkeys = []
    for monkey in content.split("\n\n"):
        monkey = monkey.splitlines()
        items = []
        for item in monkey[1].split(": ")[1].split(", "):
            items.append(int(item))
        operation = monkey[2].split("= ")[1]
        test_num = int(monkey[3].split()[-1])
        positive = int(monkey[4].split()[-1])
        negitive = int(monkey[5].split()[-1])

        m = Monkey(items, operation, test_num, positive, negitive)
        monkeys.append(m)
    
    return monkeys


def part_a(content):
    monkeys = input_to_data_objects(content)

    for round in range(20):
        for monkey in monkeys:
            for item in monkey.items:
                new = int(monkey.run_operation(item) / 3)
                target_monkey = monkey.get_target(new)
                monkeys[target_monkey].items.append(new)
                monkey.inspections += 1
            monkey.items = []

    monkeys.sort(reverse=True)

    return math.prod([m.inspections for m in monkeys[:2]])


def part_b(content):
    monkeys = input_to_data_objects(content)

    lcd = 1
    for m in monkeys:
        lcd *= m.divisor
    
    for m in monkeys:
        m.lcd = lcd

    for round in range(10_000):
        for monkey in monkeys:
            for item in monkey.items:
                new = int(monkey.run_operation(item))
                new %= monkey.lcd
                target_monkey = monkey.get_target(new)
                monkeys[target_monkey].items.append(new)
                monkey.inspections += 1
            monkey.items = []

    monkeys.sort(reverse=True)

    return math.prod([m.inspections for m in monkeys[:2]])


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
