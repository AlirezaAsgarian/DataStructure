import math
from asyncio import PriorityQueue
from heapq import *


class vertex:
    weight = 0
    neighbors = []

    def __init__(self, weight):
        self.weight = weight
        self.neighbors = []
        self.distance = math.inf

    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __lt__(self, other):
        return self.weight < other.weight


def createGraph(numberOfNodes, weights):
    graph = []
    for i in range(0, numberOfNodes):
        graph.append(vertex(weights[i]))
    return graph


def addNeighbor(graph, currentNode, *neighbors):
    for n in neighbors:
        if not currentNode.neighbors.__contains__(n) :
            currentNode.neighbors.append(graph[n])


def getMinimumNodeWeight(graph, currnetNode, isVisit):
    minNode = vertex(100000)
    for n in currnetNode.neighbors:
        print(currnetNode.weight, " ", n.weight)
        if not isVisit[graph.index(n)] and minNode.weight > n.weight:
            minNode = n
    return minNode


def calculatePowerNeedsToExceed(graph, indexOfRootNode):
    visit = {}
    for n in graph :
        visit[n] = False
    root = graph[indexOfRootNode]
    heapList = [root]
    heapify(heapList)
    power = root.weight
    needsToExceed = 0
    while len(heapList) != 0:
        currentNode = heappop(heapList)
        visit[currentNode] = True
        if currentNode != root :
            power,needsToExceed = visitAndUpdatePowerAndNeedsToExceed(currentNode, needsToExceed, power)
        addCurrentNodeNeighbors(currentNode, heapList, visit)
    return needsToExceed


def addCurrentNodeNeighbors(currentNode, heapList, visit):
    for n in currentNode.neighbors:
        if not visit[n]:
            visit[n] = True
            heappush(heapList, n)


def visitAndUpdatePowerAndNeedsToExceed(currentNode, needsToExceed, power):
    if not power > currentNode.weight:
        need = (currentNode.weight - power) + 1
        needsToExceed += need
        power += need
    power += currentNode.weight
    return power,needsToExceed


def findMinPowerNeedsToExceed(orderOfNodes):
    currentNode = orderOfNodes[0]
    power = orderOfNodes[0].weight
    needsToExceed = 0
    for i in range(1,len(orderOfNodes)) :
        node = orderOfNodes[i]
        if not power > node.weight:
            need = (node.weight - power) + 1
            needsToExceed += need
            power += need
        power += node.weight
    return needsToExceed


def printResult(graph):
    resultArray = []
    for i in range(0,len(graph)) :
        print(calculatePowerNeedsToExceed(graph, i), end=" ")

numberOfEdges = 0
numberOfVertices = 0

firstInput = input().split()

numberOfEdges = int(firstInput[1])
numberOfVertices = int(firstInput[0])

weights = []

for i in input().split() :
    weights.append(int(i))

graph = createGraph(numberOfVertices,weights)

for i in range(0,numberOfEdges) :
    inpt = input().split()
    first = int(inpt[0]) - 1
    second = int(inpt[1]) - 1
    addNeighbor(graph, graph[first], second)
    addNeighbor(graph, graph[second], first)


printResult(graph)