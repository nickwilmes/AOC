from aocd import data


####################
# TEST DATA
####################
test_data = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
test_a_answer = "88"
test_b_answer = "36"

directions = {
    "U": (0,-1),
    "D": (0,1),
    "L": (-1,0),
    "R": (1,0)   
}

####################
# Puzzle solutions
####################


def find_velocity(head: list[int,int], tail: list[int, int]) -> list[int, int]:
    ans = [0,0]
    if abs(head[0]-tail[0]) + abs(head[1]-tail[1]) >= 3:
        if tail[0] < head[0]:
            ans[0] += 1
        else:
            ans[0] -= 1
        if tail[1] < head[1]:
            ans[1] += 1
        else:
            ans[1] -= 1

    elif abs(head[0]-tail[0]) > 1:
        if head[0] > tail[0]:
            ans[0] += 1
        else:
            ans[0] -= 1
    
    elif abs(head[1] - tail[1]) > 1:
        if head[1] > tail[1]:
            ans[1] += 1
        else:
            ans[1] -= 1

    return ans


def part_a(content):
    tail_history = set()
    head = [0,0]
    tail = [0,0]
    for action in content.splitlines():
        direction, distance = action.split()
        for i in range(int(distance)):
            head[0] += directions[direction][0]
            head[1] += directions[direction][1]
        
            vel = find_velocity(head, tail)
            tail[0] += vel[0]
            tail[1] += vel[1]
                
            tail_history.add((tail[0], tail[1]))
    return len(tail_history)
    


def part_b(content):
    tail_history = set()
    knots = []
    for _ in range(10):
        knots.append([0,0])

    for action in content.splitlines():
        direction, distance = action.split()
        for i in range(int(distance)):
            head = knots[0]
            head[0] += directions[direction][0]
            head[1] += directions[direction][1]
        
            for i in range(1, len(knots)):
                head = knots[i-1]
                tail = knots[i]

                vel = find_velocity(head, tail)
                tail[0] += vel[0]
                tail[1] += vel[1]
                
            tail_history.add((knots[-1][0], knots[-1][1]))

    return len(tail_history)


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
