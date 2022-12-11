class Node:
    index = 0
    value = 0

    def __init__(self, index, value):
        self.value = value
        self.index = index


def countingSortAndPrintResult(arr):
    result = [None] * 1000001
    for i in arr:
        if result[i.value] is None :
            result[i.value] = []
        result[i.value].append(i)
    counter = 0
    for i in result:
        if i is not None:
            for j in i:
                arr[counter] = j
                print(j.index , end= " ")
                counter += 1
                



number = int(input())
numbers = input().split()
nodes = []
for i in range(0,len(numbers)) :
    nodes.append(Node(i + 1,int(numbers[i])))

countingSortAndPrintResult(nodes)