import io
import sys
import unittest
import DsHws.Hw2.asghareTama





class asghareTammaTest(unittest.TestCase):

    def test_createGraph(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        for node in graph:
            if node.index != len(graph) - 1:
                self.assertTrue(node.neighbors.__contains__(graph[node.index + 1]))
            if node.index != 0:
                self.assertTrue(node.neighbors.__contains__(graph[node.index - 1]))

    def test_makeSet(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        for node in graph:
            DsHws.Hw2.asghareTama.makeSet(node)
            self.assertEqual(node.rep, node)
            self.assertEqual(node.rank, 0)

    def test_find_set(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        DsHws.Hw2.asghareTama.makeSet(graph[0])
        graph[1].rep = graph[0]
        graph[2].rep = graph[1]
        self.assertEqual(DsHws.Hw2.asghareTama.findSet(graph[2]), graph[0])
        self.assertEqual(graph[2].rep, graph[0])

    def test_union(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        DsHws.Hw2.asghareTama.makeSet(graph[0])
        DsHws.Hw2.asghareTama.makeSet(graph[1])
        DsHws.Hw2.asghareTama.unionSet(graph[0], graph[1])
        self.assertEqual(graph[1].rep, graph[0])
        DsHws.Hw2.asghareTama.makeSet(graph[2])
        DsHws.Hw2.asghareTama.unionSet(graph[2], graph[0])
        self.assertEqual(graph[2].getLength(),3)
        self.assertEqual(graph[2].rep, graph[0])

    def test_createGraphWithCuttings(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        cuttingPoints = [2, 3, 4]
        DsHws.Hw2.asghareTama.cutGraph(graph, cuttingPoints)
        self.assertFalse(graph[1].neighbors.__contains__(graph[2]))
        self.assertFalse(graph[2].neighbors.__contains__(graph[1]))
        self.assertFalse(graph[2].neighbors.__contains__(graph[3]))
        self.assertFalse(graph[3].neighbors.__contains__(graph[2]))
        self.assertFalse(graph[3].neighbors.__contains__(graph[4]))
        self.assertFalse(graph[4].neighbors.__contains__(graph[3]))

    def test_createDisjointSets(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        cuttingPoints = [2, 3, 4]
        DsHws.Hw2.asghareTama.cutGraph(graph, cuttingPoints)
        maxSet = DsHws.Hw2.asghareTama.createDisjointSetsAndReturnFirstMaximum(graph)
        self.assertEqual(graph[4].rep, graph[4])
        self.assertEqual(graph[3].rep, graph[3])
        self.assertEqual(graph[2].rep, graph[2])
        self.assertEqual(graph[1].rep, graph[0])
        self.assertEqual(graph[0].rep, graph[0])
        self.assertEqual(maxSet.getLength(),2)

    def test_find_max_after_join(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        cuttingPoints = [2, 3, 4]
        DsHws.Hw2.asghareTama.cutGraph(graph, cuttingPoints)
        maxSet = DsHws.Hw2.asghareTama.createDisjointSetsAndReturnFirstMaximum(graph)
        maxSet = DsHws.Hw2.asghareTama.joinAndGetNewMax(2,graph,maxSet)
        self.assertEqual(maxSet.getLength(),3)

    def test_print_result(self):
        numberOfNodes = 5
        graph = DsHws.Hw2.asghareTama.createGraph(numberOfNodes)
        cuttingPoints = [2, 3, 4]
        DsHws.Hw2.asghareTama.print_result(numberOfNodes,cuttingPoints)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput



