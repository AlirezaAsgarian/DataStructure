import io
import math
import sys
import unittest
from DsHws.TheoryHws.Hw2.Q7TraverseInBst import bst,Node
from DsHws.TheoryHws.Hw2 import Q7TraverseInBst

class Q7TraversInBstTests(unittest.TestCase) :

    def test_traversePreOrder(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        tree = bst()
        tree.insert(Node(6))
        tree.insert(Node(4))
        tree.insert(Node(10))
        tree.insert(Node(15))
        tree.insert(Node(8))
        tree.insert(Node(5))
        tree.insert(Node(3))
        tree.insert(Node(12))
        Q7TraverseInBst.printPreOrder(tree.getRoot())
        self.assertEqual("6\n4\n3\n5\n10\n8\n15\n12\n",capturedOutput.getvalue())

    def test_traverseInOrder(self) :
      capturedOutput = io.StringIO()
      sys.stdout = capturedOutput
      tree = bst()
      tree.insert(Node(6))
      tree.insert(Node(4))
      tree.insert(Node(10))
      tree.insert(Node(15))
      tree.insert(Node(8))
      tree.insert(Node(5))
      tree.insert(Node(3))
      tree.insert(Node(12))
      Q7TraverseInBst.printInOrder(tree.getRoot())
      self.assertEqual("3\n4\n5\n6\n8\n10\n12\n15\n", capturedOutput.getvalue())

    def test_traversePostOrder(self) :
      capturedOutput = io.StringIO()
      sys.stdout = capturedOutput
      tree = self.createTree()
      Q7TraverseInBst.printPostOrder(tree.getRoot())
      self.assertEqual("4\n12\n10\n18\n24\n22\n15\n31\n44\n35\n66\n90\n70\n50\n25\n", capturedOutput.getvalue())

    def test_createTreeFromPreOrder(self):
        nodes = self.createNodes(25,15,10,4,12,22,18,24,50,35,31,44,70,66,90)
        Q7TraverseInBst.createTreeFromPreOrder(nodes,math.inf,0)
        self.assertEqual(nodes[0].left.value,15)
        self.assertEqual(nodes[1].left.value,10)
        self.assertEqual(nodes[2].left.value,4)
        self.assertEqual(nodes[5].right.value,24)
        self.assertEqual(nodes[5].left.value,18)


    def createTree(self):
        tree = bst()
        tree.insert(Node(25))
        tree.insert(Node(15))
        tree.insert(Node(50))
        tree.insert(Node(10))
        tree.insert(Node(22))
        tree.insert(Node(35))
        tree.insert(Node(70))
        tree.insert(Node(4))
        tree.insert(Node(12))
        tree.insert(Node(18))
        tree.insert(Node(24))
        tree.insert(Node(31))
        tree.insert(Node(44))
        tree.insert(Node(66))
        tree.insert(Node(90))
        return tree

    def createNodes(self, *numbers):
        nodes = []
        for i in numbers :
            node = Node(i)
            nodes.append(node)
        return nodes
