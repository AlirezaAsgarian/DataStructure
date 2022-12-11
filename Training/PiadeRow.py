# be name khoda

class Node :
    value = 0
    numberOfErrors = 0
    def __init__(self,value,numberOfErrors):
        self.value = value
        self.numberOfErrors  = numberOfErrors




def calculateNumberOfErrors(bitString) :
    nodes = []
    nodes.append(Node(int(bitString[0]),0))
    for i in range(1 , len(bitString)) :
        if bitString[i] == bitString[i - 1] :
            nodes.append(Node(int(bitString[i]),nodes[i - 1].numberOfErrors + 1))
        else:
            nodes.append(Node(int(bitString[i]),nodes[i - 1].numberOfErrors))
    return nodes

def printError(left,right) :
    if right.numberOfErrors != left.numberOfErrors :
        print("NO")
    else:
        print("YES")


# firstInput = input().split()
#
# numberOfQueries = int(firstInput[1])
#
# nodes = calculateNumberOfErrors(input().split())
#
# for i in range(0,numberOfQueries) :
#     inputSpan = input().split()
#     left , right = int(inputSpan[0]) , int(inputSpan[1])
#     printError(nodes[left - 1],nodes[right - 1])
