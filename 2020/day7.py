from __future__ import annotations
from aocd import data
from dataclasses import dataclass


####################
# TEST DATA
####################
test_data = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""
test_a_answer = "4"
test_b_answer = "32"


####################
# Puzzle solutions
####################
def parse_allowed(allowed_str: str):
    result = []
    for allowed in allowed_str.split(", "):
        amount, _, bag_type = allowed.partition(" ")
        result.append((bag_type, amount))
    return result


def part_a(content):
    rules = {}
    for rule in content:
        if "no other bags" in rule:
            continue
        rule = rule.replace("bags", "bag")
        rule = rule.replace(".", "")
        type_str, allowed_str = rule.split(" contain ")
        rules[type_str] = parse_allowed(allowed_str)
    
    new_bag_type_found = True
    allowed_bags = set(["shiny gold bag"])
    while new_bag_type_found:
        new_bag_type_found = False
        new_bag_types = []
        for bag, rule in rules.items():
            for allowed in rule:
                if allowed[0] in allowed_bags and bag not in allowed_bags:
                    new_bag_types.append(bag)
        if len(new_bag_types) > 0:
            new_bag_type_found = True
            allowed_bags = allowed_bags.union(new_bag_types)
    
    return len(allowed_bags)-1
    


def cost_of_bag(rules: dict, bag: str):
    cost = 1
    for required in rules.get(bag, []):
        cost += cost_of_bag(rules, required[0]) * int(required[1])
    return cost


def part_b(content):
    rules = {}
    for rule in content:
        if "no other bags" in rule:
            continue
        rule = rule.replace("bags", "bag")
        rule = rule.replace(".", "")
        type_str, allowed_str = rule.split(" contain ")
        rules[type_str] = parse_allowed(allowed_str)
    
    return cost_of_bag(rules, "shiny gold bag")-1
        


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
