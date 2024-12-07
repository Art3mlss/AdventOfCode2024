## --- Day 1: Historian Hysteria ---
# @Author : Art3mis
# @Date : 07/12/2024
# @File : day1.py
# @Project: Advent of Code 2024
## ---------------------------------

## ----- Accessing Input File

path = "../Resources/"
day = "1"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()

## ----- Part #1
# Find the total sum of the distances between each item of the two lists sorted

lines = content.split("\n")
list1, list2 = zip(*(map(int, line.split()) for line in lines))
list1 = list(list1)
list2 = list(list2)
list1.sort()
list2.sort()

def findDistance(l1, l2):
    # Calculate the absolute distance between corresponding elements of two lists
    distances = []
    for i in range(len(list1)):
        distances.append(abs(l1[i] - l2[i]))
    return distances

print(sum(findDistance(list1, list2)))
# Solution for my input : 1590491

## ----- Part #2
# Find how often each item of the first list appears in the second list, then compute the similarity score

def countOccurrences(list1, list2):
    # Create a dictionary to count occurrences of each item in list1 within list2
    count_dict = {item: list2.count(item) for item in list1}
    return count_dict

def computeSimilarityScore(list1, list2):
    # Compute
    score = 0
    count_dict = countOccurrences(list1, list2)
    for key, value in count_dict.items():
        score += key*value*list1.count(key)
    return score

print(computeSimilarityScore(list1, list2))
# Solution for my input : 22588371