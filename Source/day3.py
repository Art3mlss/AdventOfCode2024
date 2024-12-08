## --- Day 3: Mull It Over ---
# @Author : Art3mis
# @Date : 08/12/2024
# @File : day3.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/3
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "3"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Import libraries
import re

## ----- Part #1
# Find each correct mul(X, Y) where X,Y are integers between 0 and 999 and compute the sum of those
# correct multiplication

def findCorrectMul(s):
    # Find each correct mul(X, Y) where X,Y are integers between 0 and 999
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(pattern, s)
    return matches

correctMuls = findCorrectMul(content)
mulSum = 0
for mul in correctMuls:
    X, Y = map(int, mul)
    mulSum += X*Y

print(mulSum)
# Solution for my input : 173419328

## ----- Part #2
# Same as before, but only consider the correct multiplication if they are enabled (do() enables and don't() disables)

