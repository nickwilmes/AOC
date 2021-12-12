def check_password(line):
    rule, password = line.split(": ")
    limits, char = rule.split(" ")
    min, max = limits.split("-")
    max = int(max)
    min = int(min)

    count = password.count(char)
    print(line)
    if count <= max and count >= min:
        print("VALID")
        return True
    print("INVALID")
    return False


filename = 'day2.input'
with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]

valid_count = 0
for line in content:
    if check_password(line):
        valid_count += 1

print(valid_count)
