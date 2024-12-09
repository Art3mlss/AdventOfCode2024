## --- Day 5: Print Queue ---
# @Author : Art3mis
# @Date : 09/12/2024
# @File : day5.py
# @Project: Advent of Code 2024
# @Link : https://adventofcode.com/2024/day/5
## ---------------------------

## ----- Accessing Input File
path = "../Resources/"
day = "5"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Part #1
# Find out all updates that respect the rules

rules, updates = content.split("\n\n")
rules = rules.split("\n")
updates = [list(map(int, update.split(','))) for update in updates.split("\n")]

# Create a dictionary of rules
rulesDict = {}
for rule in rules:
    rule = rule.split("|")
    rule = [int(x) for x in rule]
    if rule[0] not in rulesDict.keys():
        rulesDict[rule[0]] = []
    rulesDict[rule[0]].append(rule[1])

def isCorrectUpdate(update):
    # Check if the update respects all the rules
    correct = True
    for i, elem in enumerate(update):
        if not correct:
            break
        if elem not in rulesDict.keys():
            continue
        else:
            for rule in rulesDict[elem]:
                if rule in update[0:i]:

                    correct = False
                    break
    return correct

correctUpdates = [i for i, update in enumerate(updates) if isCorrectUpdate(update)]
sumCorrectUpdates = sum(updates[i][int(len(updates[i])/2)] for i in correctUpdates)
print(sumCorrectUpdates)

# Solution for my input : 5091
## ----- Part #2