from aocd import data


####################
# TEST DATA
####################
test_data = """\
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""
test_a_answer = "26"
test_b_answer = "61229"


####################
# Puzzle solutions
####################
def part_a(content):
    count = 0
    for problem in content:
        samples, _, output = problem.partition(" | ")
        known_nums = {}
        for number in output.split():
            if len(number) == 2:
                known_nums[1] = number
                count += 1
            elif len(number) == 7:
                known_nums[8] = number
                count += 1
            elif len(number) == 3:
                known_nums[7] = number
                count += 1
            elif len(number) == 4:
                known_nums[4] = number
                count += 1
    return count


def part_b(content):
    count = 0
    for problem in content:
        samples, _, output = problem.partition(" | ")
        known_nums = {}
        possible_690 = []
        possible_235 = []
        for number in samples.split():
            if len(number) == 2:
                known_nums[1] = sorted(number)
            elif len(number) == 7:
                known_nums[8] = sorted(number)
            elif len(number) == 3:
                known_nums[7] = sorted(number)
            elif len(number) == 4:
                known_nums[4] = sorted(number)
            elif len(number) == 6:
                possible_690.append(sorted(number))
            elif len(number) == 5:
                possible_235.append(sorted(number))
        
        for n in possible_690:
            if len(set(known_nums[1]).difference(set(n))) == 1:
                known_nums[6] = n
            elif len(set(n).difference(set(known_nums[4]))) == 2:
                known_nums[9] = n
            else:
                known_nums[0] = n
        
        for n in possible_235:
            if len(set(n).difference(set(known_nums[1]))) == 3:
                known_nums[3] = n
            else:
                if len(set(n).union(set(known_nums[4]))) == 7:
                    known_nums[2] = n
                else:
                    known_nums[5] = n
        
        translated_output = ""
        nums = list(known_nums.keys())
        encryptions = list(known_nums.values())
        for number in output.split():
            narr = sorted(number)
            i = encryptions.index(narr)
            translated_output += str(nums[i])
        count += int(translated_output)

    return count


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
