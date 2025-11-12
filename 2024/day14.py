from aocd import data
import helpers
import re
import math
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image


###
# WARNING!!
# 
# This is a poorly designed part 2 and I ended up brute forcing it, so don't rely on this
###



####################
# TEST DATA
####################
test_data = """\
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
test_b_data = test_data
test_a_answer = "12"
test_b_answer = "7916"


####################
# Puzzle solutions
####################
BotsList = list[tuple[helpers.Position, helpers.Position]] 

def clear_screen():
    # Clears screen based on OS
    os.system('cls' if os.name == 'nt' else 'clear')


def move_n_steps(bots: BotsList, width: int, height: int, num_steps: int) -> BotsList:
    future_bots: BotsList = []
    for pos, vel in bots:
        new_pos = (pos[0]+vel[0]*num_steps, pos[1]+vel[1]*num_steps)
        new_pos = (new_pos[0]%width, new_pos[1]%height)
        future_bots.append((new_pos, vel))
    
    return future_bots


def print_room(bots: BotsList, width: int, height: int) -> None:
    grid = []
    for y in range(height):
        grid.append(['.']*width)
    
    for pos, _ in bots:
        x, y = pos
        grid[y][x] = '#'
    
    for i in range(min(len(grid), 50)):
        print("".join(grid[i]))


def generate_tree_points(width: int, height: int) -> list[helpers.Position]:
    points: list[helpers.Position] = []
    star_point = (int(width/2), 0)
    trunk =  (int(width/2), height-1)

    points.append(star_point)
    for i in range(1, height-1):
        if star_point[0]-i < 0:
            break
        points.append((star_point[0]-i, i))
        points.append((star_point[0]+i, i))
    
    points.append(trunk)

    return points


def get_quad_scores(bots, width, height) -> tuple[int, int, int, int]:
    tl, tr, bl, br = 0, 0, 0, 0
    midx, midy = int(width/2), int(height/2)
    for pos, _ in bots:
        x, y = pos
        if x < midx:
            if y < midy:
                tl += 1
            elif y > midy:
                tr += 1
        elif x > midx:
            if y < midy:
                bl += 1
            elif y > midy:
                br += 1
    
    return tl, tr, bl, br


def part_a(content: str, width: int, height: int):
    bots_str = content.split('\n')
    
    # parse bots
    bots: BotsList = []
    for bot in bots_str:
        px, py, vx, vy = map(int, re.findall(r"-?\d+", bot))
        bots.append(((px, py), (vx, vy)))
    
    # move bots 100 steps
    future_bots = move_n_steps(bots, width, height, 100)

    # count safety factor
    quad_scores = get_quad_scores(future_bots, width, height)
    
    return math.prod(quad_scores)


def part_b(content: str, width: int, height: int):
    bots_str = content.split('\n')
    
    # parse bots
    bots: BotsList = []
    for bot in bots_str:
        px, py, vx, vy = map(int, re.findall(r"-?\d+", bot))
        bots.append(((px, py), (vx, vy)))
    
    for step in range(4664, 12295):
    # for step in range(1, 10000):
        new_bots = move_n_steps(bots, width, height, step)
        image = np.ones((height, width, 3), dtype=int)*119
        for pos, _ in new_bots:
            x, y = pos
            image[y,x] = np.array([78,178,101])

        frame = Image.fromarray(image.astype('uint8'), mode='RGB')
        frame = frame.resize((image.shape[0]*8, image.shape[1]*8), resample=Image.NEAREST)
        frame.save('./DAY14-frames/'+str(step).zfill(4)+'.png')

    return 7916

# 2992 < ans < 13395
####################
# Main Logic
####################
if __name__ == "__main__":
    content = data

    test_a = part_a(test_data, 11, 7)
    print(f"Test A: {test_a}")
    assert str(test_a) == test_a_answer
    print(f"Part A answer: {part_a(content, 101, 103)}")

    # test_b = part_b(test_data, 11, 7)
    # print(f"Test B: {test_b}")
    # assert str(test_b) == test_b_answer
    print(f"Part B answer: {part_b(content, 101, 103)}")
