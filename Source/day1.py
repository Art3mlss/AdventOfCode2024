path = "../Resources/"
day = "1"
with open(path+"day"+day+".txt", 'r') as file:
    content = file.read()
    print(content)

lines = content.split("\n")
list1, list2 = zip(*(map(int, line.split()) for line in lines))
list1 = list(list1)
list2 = list(list2)
list1.sort()
list2.sort()

def find_distance(l1, l2):
    distances = []
    for i in range(len(list1)):
        distances.append(abs(l1[i] - l2[i]))
    return distances

print(sum(find_distance(list1, list2)))