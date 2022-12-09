from aocd import data


####################
# TEST DATA
####################
test_data = """\
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
test_a_answer = "95437"
test_b_answer = "24933642"


####################
# Puzzle solutions
####################
def parse_console_output(content):
    commands = []
    command = ""
    output = ""
    for line in content.splitlines():
        if line.startswith("$"):
            if command:
                commands.append((command, output))
            command = line.partition(" ")[2]
            output = ""
        else:
            output += f'{line}\n'
    
    commands.append((command, output))
    
    return commands


def part_a(content):
    commands = parse_console_output(content)
    cur_dir = "/"
    dirs = {"/": 0}
    for command, output in commands:
        if command == 'ls':
            for line in output.splitlines():
                if line.startswith("dir"):
                    dirs[f'{cur_dir}{line.split()[1]}/'] = 0
                else:
                    dirs[cur_dir] += int(line.split()[0])
        elif command.startswith('cd'):
            target = command.split()[1]
            if target == "..":
                cur_dir = "/".join(cur_dir.split("/")[:-2])
                cur_dir += "/"
            elif target.startswith("/"):
                cur_dir = target
            else:
                cur_dir += f"{target}/"
    
    ans = 0
    for dir in dirs.keys():
        size = sum([s if name.startswith(dir) else 0 for name, s in dirs.items()])
        if size <= 100_000:
            ans += size

    return ans


def part_b(content):
    commands = parse_console_output(content)
    cur_dir = "/"
    dirs = {"/": 0}
    for command, output in commands:
        if command == 'ls':
            for line in output.splitlines():
                if line.startswith("dir"):
                    dirs[f'{cur_dir}{line.split()[1]}/'] = 0
                else:
                    dirs[cur_dir] += int(line.split()[0])
        elif command.startswith('cd'):
            target = command.split()[1]
            if target == "..":
                cur_dir = "/".join(cur_dir.split("/")[:-2])
                cur_dir += "/"
            elif target.startswith("/"):
                cur_dir = target
            else:
                cur_dir += f"{target}/"
    
    space_available = 70_000_000 - sum([s for _, s in dirs.items()])
    space_needed = 30_000_000 - space_available
    ans = 70_000_000
    for dir in dirs.keys():
        size = sum([s if name.startswith(dir) else 0 for name, s in dirs.items()])
        if size >= space_needed and size <= ans:
            ans = size

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
