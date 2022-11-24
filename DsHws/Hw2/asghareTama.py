from collections import defaultdict


class Node:
    neighbors = None
    index = 0
    rank = 0
    length = 1
    rep = None

    def __init__(self, index):
        self.neighbors = []
        self.index = index

    def addEdge(self, node):
        self.neighbors.append(node)

    def getLength(self):
        if self.rep != self:
            return self.rep.length
        return self.length


def createGraph(numberOfNodes):
    graph = list()
    for i in range(0, numberOfNodes):
        newNode = Node(i)
        if newNode.index != 0:
            newNode.addEdge(graph[i - 1])
            graph[i - 1].addEdge(newNode)
        graph.append(newNode)
    return graph


def makeSet(node):
    node.rep = node
    node.rank = 0



def findSet(node):
    if node.rep != node:
        node.rep = findSet(node.rep)
    return node.rep


def link(rep1, rep2):
    if rep1.getLength() >= rep2.getLength():
        rep2.rep = rep1
        rep1.length += rep2.length
        rep1.rank += 1
    else:
        rep1.rep = rep2
        rep2.length += rep1.length
        rep2.rank += 1


def unionSet(node1, node2):
    link(findSet(node1), findSet(node2))


def cutGraph(graph, cuttingPoints):
    for point in cuttingPoints:
        graph[point].neighbors.remove(graph[point - 1])
        graph[point - 1].neighbors.remove(graph[point])


def createDisjointSetsAndReturnFirstMaximum(graph):
    index = 0
    maximumSetRepresentative = graph[0]
    while index < len(graph):
        makeSet(graph[index])
        while index + 1 < len(graph) and graph[index].neighbors.__contains__(graph[index + 1]):
            makeSet(graph[index + 1])
            unionSet(graph[index],graph[index + 1])
            index += 1
        maximumSetRepresentative = graph[index] if graph[index].getLength() > maximumSetRepresentative.getLength() else maximumSetRepresentative
        index += 1
    return maximumSetRepresentative


def joinAndGetNewMax(pointOfJoin, graph,preMax):
    unionSet(graph[pointOfJoin - 1],graph[pointOfJoin])
    if preMax == findSet(graph[pointOfJoin]) :
        return preMax
    else:
        if preMax.getLength() > findSet(graph[pointOfJoin]).getLength() :
            return preMax
        else:
            return findSet(graph[pointOfJoin])


def print_result(numberOfNodes, cuttingPoints):
    result = []
    graph = createGraph(numberOfNodes)
    cutGraph(graph,cuttingPoints)
    max = createDisjointSetsAndReturnFirstMaximum(graph)
    result.append(max.getLength())
    for point in range(len(cuttingPoints) - 1 , 0, -1 ) :
        max = joinAndGetNewMax(cuttingPoints[point],graph,max)
        result.append(max.getLength())
    for i in range(len(result) - 1 , -1  , -1) :
        print(result[i])


number_of_nodes = int(input().split()[0])
cuttingPoints = []

for i in input().split() :
    cuttingPoints.append(int(i))

print_result(number_of_nodes,cuttingPoints)