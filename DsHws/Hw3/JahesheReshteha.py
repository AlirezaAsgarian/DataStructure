m = 1024
p = 37


class Node:
    rightChildren = None
    leftChildren = None
    value = 0
    id = 0

    def __init__(self, value, id):
        self.value = value
        self.id = id


def calculateHashSuffixes(str):
    suffixes = []
    differSuffixes = []
    sumOfSuffixes = 0
    primeNumber = p
    for i in range(0, len(str)):
        sumOfSuffixes += (ord(str[i]) * primeNumber) % m
        primeNumber = ((p * primeNumber) % m)
        suffixes.append(sumOfSuffixes)
    return suffixes


def createTree(suffixes, left, right, nodes, parentValue):
    if left > right or left == len(suffixes) or right == -1:
        return None
    m = (right + left) // 2
    value = suffixes[m] - parentValue
    node = Node(value, m)
    node.rightChildren = createTree(suffixes, m + 1, right, nodes, suffixes[m])
    node.leftChildren = createTree(suffixes, left, m - 1, nodes, suffixes[m])
    nodes.append(node)
    return node


def calculateSuffixOfIndex(nodes, value, currentNode, key):
    value += currentNode.value
    if currentNode.id > key:
        return calculateSuffixOfIndex(nodes, value, currentNode.leftChildren, key)
    if currentNode.id < key:
        return calculateSuffixOfIndex(nodes, value, currentNode.rightChildren, key)
    return (value % m)


def calculateHashOfSubString(nodes, left, right):
    rightSuffix = 0
    rightSuffix = calculateSuffixOfIndex(nodes, 0, nodes[len(nodes) - 1], right)
    leftSuffix = 0
    if left - 1 >= 0:
        leftSuffix = calculateSuffixOfIndex(nodes, 0, nodes[len(nodes) - 1], left - 1)
    else:
        leftSuffix = 0
    return (rightSuffix - leftSuffix) % m


def compareTwoSubString(p, m, nodes1, nodes2, left1, left2, shift):
    hash1 = calculateHashOfSubString(nodes1, left1, left1 + shift - 1) % m
    hash2 = calculateHashOfSubString(nodes2, left2, left2 + shift - 1) % m
    if left1 > left2:
        hash2 = (hash2 * (p ** (left1 - left2))) % m
    if left1 < left2:
        hash1 = (hash1 * (p ** (left2 - left1))) % m
    return "YES" if hash1 == hash2 else "NO"


def updateChars(nodes1, key, differ, currentNode, parent):
    if currentNode is None:
        return
    if currentNode.id >= key:
        if parent.id <= key:
            currentNode.value = (currentNode.value + differ) % m
        updateChars(nodes1, key, differ, currentNode.leftChildren, currentNode)
    if currentNode.id < key:
        if parent.id >= key:
            currentNode.value = (currentNode.value - differ) % m
        updateChars(nodes1, key, differ, currentNode.rightChildren, currentNode)


def changeCharacter(nodes1, index, differ):
    root = nodes1[len(nodes1) - 1]
    if root.id < index:
        updateChars(nodes1, index, differ, root.rightChildren, root)
    elif root.id > index:
        nodes1[len(nodes1) - 1].value = (nodes1[len(nodes1) - 1].value + differ) % m
        updateChars(nodes1, index, differ, root.leftChildren, root)
    else:
        nodes1[len(nodes1) - 1].value = (nodes1[len(nodes1) - 1].value + differ) % m
        updateChars(nodes1, index, differ, root.leftChildren, root)
        updateChars(nodes1, index, differ, root.rightChildren, root)


def printResult(strings, operations):
    nodes = []
    suffixesess = []
    for str in strings :
        suffixes = calculateHashSuffixes(str)
        suffixesess.append(suffixes)
        nodesOfThisString = []
        createTree(suffixes, 0, len(str), nodesOfThisString, 0)
        nodes.append(nodesOfThisString)

    for oper in operations :
        splOper = oper.split()
        if int(splOper[0]) == 0 :
            print(compareTwoSubString(p,m,nodes[int(splOper[1]) - 1],nodes[int(splOper[2]) - 1],int(splOper[3]) - 1,int(splOper[4]) - 1,int(splOper[5])))
        else :
            changeCharacter(nodes[int(splOper[1]) - 1], int(splOper[2]) - 1,getDiffer(splOper, strings,int(splOper[2]) - 1,splOper[3],int(splOper[1]) - 1))


def getDiffer(splOper, strings, index, newChar,stringNumber):
    return (((p ** (index + 1)) % m) * (ord(newChar) - ord(strings[stringNumber][index]))) % m






