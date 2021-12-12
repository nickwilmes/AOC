def count_trees(map, slopex, slopey):
    width = len(map[0])
    col = slopey % width
    row = slopex
    count = 0
    while row < len(map):
        print(f"({row},{col})")
        if map[row][col] == '#':
            count += 1
        col = (col + slopey) % width
        row += slopex

    return count


filename = 'day3.input'
with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]
map = content

print(count_trees(map, 1, 3))
