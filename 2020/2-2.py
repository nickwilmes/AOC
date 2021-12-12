def check_password(line):
    rule, password = line.split(": ")
    limits, char = rule.split(" ")
    i, j = limits.split("-")
    i = int(i)-1
    j = int(j)-1

    print(line)
    if [password[i], password[j]].count(char) == 1:
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
