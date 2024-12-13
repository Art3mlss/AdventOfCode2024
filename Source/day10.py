## --- Day 10: Hoof It ---
# @Author : Art3mis
# @Date : 13/12/2024
# @File : day10.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/10
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "10"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Import Libraries
import time

## ----- Part #1
# Find how many different 9 each 0 can reach with a step of 1 each time in the grid

start = time.time()

grid = [list(e) for e in content.split("\n")]
zeros = [(i, j) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '0']

totalScore = 0
for (startX, startY) in zeros:
    # for each 0 in the grid, find out how many 9 are reachable
    visited = [(startX, startY)]
    closed = []

    headScore = 0
    while visited:
        x, y = visited[-1]
        currentValue = int(grid[x][y])


        # Find the list of all possible moves from (x, y)
        possibleMoves = []
        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            i, j = x+dx, y+dy
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and (i, j) not in closed:   # Make sure the move is in the
                if int(grid[i][j]) == currentValue + 1:                                 # grid, and isn't to a
                    possibleMoves.append((i, j))                                        # closed position

        if not possibleMoves:                   # If no possible moves, close the current position
            if currentValue == 9:                   # If it is a 9, increment the head score before closing the position
                headScore += 1
            closed.append(visited.pop())
        else:                                   # If possible moves, visit the first one
            visited.append(possibleMoves[0])

    # Add this head score to the total score
    totalScore += headScore

print(totalScore)
print(f"Execution time: {time.time()-start:.4f} s")
# Solution for my input : 717
# Ran in 0.034s on my laptop