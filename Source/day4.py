## --- Day 4: Ceres Search ---
# @Author : Art3mis
# @Date : 08/12/2024
# @File : day4.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/4
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "4"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Part #1
# Find XMAS written in any way possible (horizontal, vertical, diagonal, written backwards) in a grid input

dir = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 0), (0, 1),
    (1, -1), (1, 0), (1, 1)
]

pattern = "XMAS"

def countPattern(s, pattern):
    # Count the number of times the pattern appears in the grid in any way possible (horizontal, vertical, diagonal, written backwards)
    count = 0
    for i in range(len(s)):
        for j in range(len(s[0])):
            for dirX, dirY in dir:
                match = True
                for k, letter in enumerate(list(pattern)):
                    if 0 <= i + k*dirX < len(s) and 0 <= j + k*dirY < len(s):
                        if s[i + k*dirX][j + k*dirY] != letter:
                            match = False
                            break
                    else:
                        match = False
                        break
                if match:
                    count += 1
    return count

print(countPattern(content.split("\n"), pattern))
# Solution for my input : 2571

## ----- Part #1
# Find all MAS in a X pattern of the grid


def countXMas(s):
    # Count the number of MAS in a X pattern of the grid (diagonal)
    count = 0
    for i in range(1, len(s)-1):
        for j in range(1, len(s[i])-1):
            if s[i][j] == "A":
                diag1, diag2 = False, False
                if (s[i-1][j-1] == "M" and s[i+1][j+1] == "S") or (s[i-1][j-1] == "S" and s[i+1][j+1] == "M"):
                    diag1 = True
                if (s[i-1][j+1] == "M" and s[i+1][j-1] == "S") or (s[i-1][j+1] == "S" and s[i+1][j-1] == "M"):
                    diag2 = True
                if diag1 and diag2:
                    count += 1
    return count

content = [list(line) for line in content.split("\n")]
print(countXMas(content))
# Solution for my input : 1992