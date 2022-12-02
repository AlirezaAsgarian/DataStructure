import io
import sys
import unittest

import Training.HitlereMakhfi
from Training.HitlereMakhfi import createGraph, calculatePowerNeedsToExceed , addNeighbor


class hitlereMakhfiTests(unittest.TestCase):

    def addNeighbors(self, graph):
        Training.HitlereMakhfi.addNeighbor(graph, graph[0], 1)
        Training.HitlereMakhfi.addNeighbor(graph, graph[1], 0, 3, 5)
        Training.HitlereMakhfi.addNeighbor(graph, graph[2], 6, 5)
        Training.HitlereMakhfi.addNeighbor(graph, graph[3], 1, 4, 5)
        Training.HitlereMakhfi.addNeighbor(graph, graph[4], 6, 3)
        Training.HitlereMakhfi.addNeighbor(graph, graph[5], 2, 6, 1, 3)
        Training.HitlereMakhfi.addNeighbor(graph, graph[6], 2, 4, 5)

    def getGraph(self):
        numberOfNodes = 7
        weights = [16, 1, 32, 256, 4, 128, 64]
        graph = createGraph(numberOfNodes, weights)
        return graph, weights

    def getGraph2(self):
        numberOfNodes = 6
        weights = [15 , 15 , 14 , 27 , 64 , 29]
        graph = createGraph(numberOfNodes,weights)
        return graph,weights

    def addNeighbors2(self,graph):
        addNeighbor(graph,graph[0],1,2)
        addNeighbor(graph,graph[1],0,3,4)
        addNeighbor(graph,graph[2],0,3)
        addNeighbor(graph,graph[3],1,2)
        addNeighbor(graph,graph[4],1,5)
        addNeighbor(graph,graph[5],4)



    def test_createGraph(self):
        graph, weights = self.getGraph()
        for i in range(0, len(graph)):
            self.assertEqual(weights[i], graph[i].weight)

    def test_addNeighbors(self):
        graph, weights = self.getGraph()
        graph[0].addNeighbor(graph[1])
        self.assertTrue(graph[0].neighbors.__contains__(graph[1]))
        self.assertFalse(graph[1].neighbors.__contains__(graph[0]))
        self.assertEqual(len(graph[0].neighbors), 1)

    def test_findShortestPathForOneVertex(self):
        graph, weights = self.getGraph()
        self.addNeighbors(graph)
        parents = calculatePowerNeedsToExceed(graph, 0)
        self.assertEqual(parents[graph[0]], None)
        self.assertEqual(parents[graph[1]], graph[0])
        self.assertEqual(parents[graph[2]], graph[1])
        self.assertEqual(parents[graph[6]], graph[2])
        self.assertEqual(parents[graph[4]], graph[6])
        self.assertEqual(parents[graph[3]], graph[4])

    def test_findShortestPathForOneVertexAndCalculatePower(self):
        graph, weights = self.getGraph()
        self.addNeighbors(graph)
        orderOfNodes = calculatePowerNeedsToExceed(graph, 1)
        self.assertEqual(orderOfNodes[0], graph[1])
        self.assertEqual(orderOfNodes[1], graph[0])
        self.assertEqual(orderOfNodes[2], graph[5])
        self.assertEqual(orderOfNodes[3], graph[2])
        self.assertEqual(orderOfNodes[4], graph[6])
        self.assertEqual(orderOfNodes[5], graph[4])
        self.assertEqual(orderOfNodes[6], graph[3])

    def test_calculateHowMuchPowerNeedsToExceed(self):
        graph, weights = self.getGraph()
        self.addNeighbors(graph)
        power0 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 0))
        self.assertEqual(power0, 112)
        power1 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 1))
        self.assertEqual(power1, 112)
        power2 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 2))
        self.assertEqual(power2, 33)
        power3 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 3))
        self.assertEqual(power3, 0)
        power4 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 4))
        self.assertEqual(power4, 61)
        power5 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 5))
        self.assertEqual(power5, 12)
        power6 = Training.HitlereMakhfi.findMinPowerNeedsToExceed(calculatePowerNeedsToExceed(graph, 6))
        self.assertEqual(power6, 29)

    def test_result(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        graph , weights = self.getGraph()
        self.addNeighbors(graph)
        Training.HitlereMakhfi.printResult(graph)
        self.assertEqual("112 112 33 0 61 12 29 ",capturedOutput.getvalue())

    def test_result2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        graph, weights = self.getGraph2()
        self.addNeighbors2(graph)
        Training.HitlereMakhfi.printResult(graph)
        self.assertEqual("0 1 2 0 0 36 ", capturedOutput.getvalue())




