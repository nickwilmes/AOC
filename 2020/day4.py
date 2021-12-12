from aocd import data
import re


def is_valid_a(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    for key in required_keys:
        if key not in passport.keys():
            return False

    return True


def content_to_passports(content):
    passports = []
    tmp = ""
    for line in content:
        if line == "":
            passports.append({x.split(":")[0]: x.split(":")[1] for x in tmp.lstrip().split(" ")})
            tmp = ""
        else:
            tmp += " " + line.replace('\n', '')
    if tmp:
        passports.append({x.split(":")[0]: x.split(":")[1] for x in tmp.lstrip().split(" ")})
    return passports


def part_a(content):
    count = 0
    passports = content_to_passports(content)
    for passport in passports:
        if is_valid_a(passport):
            count += 1
    return count


def valid_height(height: str) -> bool:
    if re.match(r"^[0-9]*in$", height):
        num = int(height.split('in')[0])
        return (59 <= num <= 76)
    elif re.match(r"^[0-9]*cm$", height):
        num = int(height.split('cm')[0])
        return (150 <= num <= 193)
    else:
        return False

    
def is_valid_b(passport):
    required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    try:
        if (
            int(passport['byr']) < 1920 or int(passport['byr']) > 2002 or
            int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020 or
            int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030 or
            not valid_height(passport['hgt']) or
            re.match(r"^#[0-9a-f]{6}$", passport['hcl']) == None or
            not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'] or
            re.match(r"^[0-9]{9}$", passport['pid']) == None
        ):
            return False
    except KeyError:
        return False

    return True


def part_b(content):
    count = 0
    passports = content_to_passports(content)
    for passport in passports:
        if is_valid_b(passport):
            count += 1
    return count


test_data_a="""\
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test_data_b="""\
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007

pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""


if __name__ == "__main__":
    content = data.splitlines()

    test_a = part_a(test_data_a.splitlines())
    print(f"Test A: {test_a}")
    print(f"Part A answer: {part_a(content)}")
    assert str(test_a) == "2"

    test_b = part_b(test_data_b.splitlines())
    print(f"Test B: {test_b}")
    print(f"Part B answer: {part_b(content)}") # 187 is too high
    assert str(test_b) == "4"