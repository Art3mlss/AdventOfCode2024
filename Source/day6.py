## --- Day 6: Guard Gallivant ---
# @Author : Art3mis
# @Date : 10/12/2024
# @File : day6.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/6
## ---------------------------
from wheel.metadata import yield_lines

## ----- Accessing Input File
path = "../Resources/"
day = "6"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Part #1
# Find all distinct positions of the guard in the grid

def rotate90Degrees(dir):
    # Rotate one of the 4 2D direction by 90 degrees
    return (dir[1], -dir[0])

def isFinished(x, y, dir, grid):
    # Check if the guard is getting out of the grid on the next move
    xDir, yDir = dir
    if 0 <= x + xDir < len(grid) and 0 <= y + yDir < len(grid[0]):
        return False
    else:
        return True

def advance(x, y, dir, grid):
    # Process the next step of the guard and return the new position and direction. If the guard encounters a wall,
    # rotate 90 degrees, and the rotation counts as a step
    xDir, yDir = dir
    if grid[x + xDir][y + yDir] == "#":
        return x, y, rotate90Degrees(dir)
    else:
        return x + xDir, y + yDir, dir


# Define the grid
grid = [list(e) for e in content.split('\n')]

# Find initial guard pos
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "^":
            gardX, gardY = i, j
            break

# Define the initial direction of the guard (up)
dir = (-1, 0)

# Find all distinct positions of the guard in the grid
visited = set()
while True:
    if isFinished(gardX, gardY, dir, grid):
        break
    else:
        gardX, gardY, dir = advance(gardX, gardY, dir, grid)

        visited.add((gardX, gardY))

print(len(visited))
# Solution for my input : 4515

## ----- Part #2
# Find which additionnal obstacle would stuck the guard in the grid

def isStuck(x, y, dir, grid):
    # Check if the guard is getting stuck in the grid
    states = set()
    states.add((x, y, dir))
    while True:
        if isFinished(x, y, dir, grid):
            return False
        else:
            x, y, dir = advance(x, y, dir, grid)
            if (x, y, dir) in states:
                return True
            else:
                states.add((x, y, dir))

# Find initial guard pos
for i, row in enumerate(grid):
    for j, cell in enumerate(row):
        if cell == "^":
            gardX, gardY = i, j
            break

# Find all possible obstacles
obstacles = []
for position in visited:
    # For each position that the guard initially visit, try to put an obstacle and check if the guard gets stuck
    if position == (gardX, gardY):
        continue

    grid[position[0]][position[1]] = "#"

    if isStuck(gardX, gardY, (-1, 0), grid):
        obstacles.append(position)
    grid[position[0]][position[1]] = "."

print(len(obstacles))
# Solution for my input : 1309
# Ran in 10.7s on my laptop. There certainly is a more efficient way to solve this problem (probably using graphs),
# though this solution is not that stupid.