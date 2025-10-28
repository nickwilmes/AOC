from aocd import data
from collections import defaultdict
import math

####################
# TEST DATA
####################
test_data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

test_b_data = test_data
test_a_answer = "143"
test_b_answer = "123"

Rule = tuple[int, int]

####################
# Puzzle solutions
####################
def parse_input(content: str) -> tuple[list[Rule], list[list[int]]]:
    raw_rules, _, raw_updates = content.partition("\n\n")
    rules = []
    for raw_rule in raw_rules.split():
        rule = raw_rule.split("|")
        rules.append((int(rule[0]), int(rule[1])))

    updates = []
    for raw_update in raw_updates.split():
        pages = [int(x) for x in raw_update.split(",")]
        updates.append(pages)
    return rules, updates


def find_revelant_rules(all_rules: list[Rule], pages: list[int]) -> list[Rule]:
    rules = []
    for rule in all_rules:
        if rule[0] in pages and rule[1] in pages:
            rules.append(rule)
    return rules


def find_first_page(pages: list[int], rules: list[Rule]) -> int:
    page = pages[0]
    i = 0
    while i < len(rules):
        rule = rules[i]
        if page == rule[1]:
            page = rule[0]
            i = 0
        else:
            i+=1

    return page


def sort_pages(pages: list[int], rules: list[Rule]) -> list[int]:
    if len(pages) == 1:
        return pages

    # find first page
    first_page = find_first_page(pages, rules)
    
    # remove first page from pages
    rest_of_pages = pages[:]
    rest_of_pages.remove(first_page)

    # find new relevant rules
    rules = find_revelant_rules(rules, rest_of_pages)

    # sort rest of pages
    sorted_pages = [first_page, *sort_pages(rest_of_pages, rules)]

    # return sorted pages
    return sorted_pages


def part_a(content: str):
    all_rules, updates = parse_input(content)

    ans = 0
    for update in updates:
        rules = find_revelant_rules(all_rules, update)
        sorted_pages = sort_pages(update, rules)
        if update == sorted_pages:
            middle_page = sorted_pages[int(len(sorted_pages)/2)]
            ans += middle_page

    return ans

def part_b(content: list[str]):
    all_rules, updates = parse_input(content)

    ans = 0
    for update in updates:
        rules = find_revelant_rules(all_rules, update)
        sorted_pages = sort_pages(update, rules)
        if update != sorted_pages:
            middle_page = sorted_pages[int(len(sorted_pages)/2)]
            ans += middle_page

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

    test_b = part_b(test_b_data)
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}")
    assert str(test_b) == test_b_answer