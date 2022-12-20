m = 10 ** 9 + 7
p = 277
primes = [p]
class Node :
    low = 0
    high = 0
    value = 0
    leftChildren = None
    rightChildren = None
    def __init__(self,value,low,high):
        self.value = value
        self.high = high
        self.low = low


def createNodes(str):
    nodes = []
    prime = p
    for i in range(0,len(str)) :
        if i == len(primes) :
            primes.append((primes[len(primes) - 1] * p) % m)
        nodes.append(Node((primes[i] * ord(str[i])) % m,i,i))
    return nodes

def createTree(nodes,currentLayer) :
    nextLayer = []
    for i in range(1,len(currentLayer),2) :
        newNode = Node(currentLayer[i - 1].value + currentLayer[i].value , currentLayer[i - 1].low,currentLayer[i].high)
        newNode.leftChildren = currentLayer[i - 1]
        newNode.rightChildren = currentLayer[i]
        nodes.append(newNode)
        nextLayer.append(newNode)

    if len(currentLayer) % 2 == 1:
        nextLayer.append(currentLayer[len(currentLayer) - 1])

    if len(nextLayer) == 1 :
        return nodes
    else:
        return createTree(nodes,nextLayer)


def query(low, high,currentNode):
    sum = 0
    if currentNode.low >= low and currentNode.high <= high :
        return currentNode.value

    if currentNode.rightChildren is not None and currentNode.rightChildren.low <= high :
        sum += (query(low,high,currentNode.rightChildren) % m)
    if currentNode.leftChildren is not None and currentNode.leftChildren.high >= low:
        sum += (query(low, high, currentNode.leftChildren) % m)
    return sum % m


def updateTree(node,target, oldValue, newValue):
    if node.low <= target <= node.high:
        node.value -= ((oldValue * primes[target]) % m)
        node.value += ((newValue * primes[target]) % m)
        node.value %= m
        if node.rightChildren is not None and node.rightChildren.low <= target:
            updateTree(node.rightChildren,target,oldValue,newValue)
        elif node.leftChildren is not None and node.leftChildren.high >= target:
            updateTree(node.leftChildren,target,oldValue,newValue)

def drawTree(nodes) :
    currentLayer = [nodes[len(nodes) - 1]]
    distanceOfLeafs = 16
    currentDistance = ((len(nodes) + 1) // 4) * distanceOfLeafs
    isEnd = True
    while isEnd :
        isEnd = False
        for i in range(0,len(currentLayer)) :
            if currentLayer[i].value != -1 :
                isEnd = True
            printSpaces(currentDistance,len(str(currentLayer[i].value)))
            printNode(currentLayer, i)
        print("")
        nextLayer = []
        for i in range(0,len(currentLayer)) :
            appendLeftChildren(currentLayer, i, nextLayer)
            appendRightChildren(currentLayer, i, nextLayer)
        currentLayer = nextLayer
        currentDistance //= 2


def appendRightChildren(currentLayer, i, nextLayer):
    if currentLayer[i].rightChildren is not None:
        nextLayer.append(currentLayer[i].rightChildren)
    else:
        nextLayer.append(Node(-1, -1, -1))


def appendLeftChildren(currentLayer, i, nextLayer):
    if currentLayer[i].leftChildren is not None:
        nextLayer.append(currentLayer[i].leftChildren)
    else:
        nextLayer.append(Node(-1, -1, -1))


def printNode(currentLayer, i):
    print("%d[%d %d]" % (currentLayer[i].value,currentLayer[i].low,currentLayer[i].high), end="")


def printSpaces(currentDistance,back):
    for j in range(0, currentDistance - back):
        print(" ", end="")


def compareTwoString(nodes1, nodes2, left1, left2, stringLen):
      hash1 = query(left1 - 1, left1 - 1 + stringLen - 1 ,nodes1[len(nodes1) - 1])
      hash2 = query(left2 - 1, left2 - 1 + stringLen - 1 ,nodes2[len(nodes2) - 1])
      if left1 > left2 :
          hash2 = (primes[left1 - left2 - 1] * hash2) % m
      if left2 > left1:
          hash1 = (primes[left2 - left1 - 1] * hash1) % m
      if hash1 == hash2 : return "YES"
      return "NO"

def printString(nodes) :
    print(len(nodes))
    for i in range(0,len(nodes)) :
        print(chr(query(i,i,nodes[i])),end="")
    print("")


def printResult(strings, operations):
    nodes = []
    for st in strings :
        strNode = createNodes(st)
        createTree(strNode,list(strNode))
        nodes.append(strNode)
    result = ""
    for ope in operations :
        splitedOper = ope.split()
        if splitedOper[0] == '0' :
            result += (compareTwoString(nodes[int(splitedOper[1]) - 1],nodes[int(splitedOper[2]) - 1],int(splitedOper[3]),int(splitedOper[4]),int(splitedOper[5])))
            result += '\n'
        if splitedOper[0] == '1' :
            currentStringIndex = int(splitedOper[1]) - 1
            currentNodes = nodes[currentStringIndex]
            updateTree(currentNodes[len(currentNodes) - 1],int(splitedOper[2]) - 1,ord(strings[currentStringIndex][int(splitedOper[2]) - 1]),ord(splitedOper[3]))
    print(result,end="")


numbersInput = input().split()
stringNumber = int(numbersInput[0])
operationsNumber = int(numbersInput[1])
strings = []
for i in range(0,stringNumber) :
    strings.append(input())

nodes = []
for st in strings :
    strNode = createNodes(st)
    createTree(strNode,list(strNode))
    nodes.append(strNode)
result = ""
operations = []
for i in range(0,operationsNumber) :
    splitedOper = input().split()
    if splitedOper[0] == '0':
        result += (compareTwoString(nodes[int(splitedOper[1]) - 1], nodes[int(splitedOper[2]) - 1], int(splitedOper[3]),
                               int(splitedOper[4]), int(splitedOper[5])))
        result += '\n'
    if splitedOper[0] == '1':
        currentStringIndex = int(splitedOper[1]) - 1
        currentNodes = nodes[currentStringIndex]
        updateTree(currentNodes[len(currentNodes) - 1], int(splitedOper[2]) - 1,
                   ord(strings[currentStringIndex][int(splitedOper[2]) - 1]), ord(splitedOper[3]))

print(result,end="")

