## ----- Accessing Input
from itertools import count

path = "../Resources/"
day = "1"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()
    print(content)

## ----- Part #1
# Find the total sum of the distances between each item of the two lists sorted

lines = content.split("\n")
list1, list2 = zip(*(map(int, line.split()) for line in lines))
list1 = list(list1)
list2 = list(list2)
list1.sort()
list2.sort()

def findDistance(l1, l2):
    distances = []
    for i in range(len(list1)):
        distances.append(abs(l1[i] - l2[i]))
    return distances

print(sum(findDistance(list1, list2)))
# Solution for my input : 1590491

## ----- Part #2
# Write a function that counts how many times each value of the first list appears in the second list

def countOccurrences(list1, list2):
    count_dict = {item: list2.count(item) for item in list1}
    return count_dict

def computeScore(list1, list2):
    score = 0
    count_dict = countOccurrences(list1, list2)
    for key, value in count_dict.items():
        score += key*value*list1.count(key)
    return score

print(computeScore(list1, list2))