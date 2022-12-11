import io
import sys
import unittest
from DsHws.Hw3 import SarbazGhul
from DsHws.Hw3.SarbazGhul import Node

class sarbazGhulTests(unittest.TestCase) :
    def test_countingSort(self):
        arr = [Node(1, 5), Node(2, 1), Node(3, 5), Node(4, 8)]
        SarbazGhul.countingSortAndPrintResult(arr)
        self.assertEqual(arr[0].index,2)
        self.assertEqual(arr[1].index,1)
        self.assertEqual(arr[2].index,3)
        self.assertEqual(arr[3].index,4)

    def test_printResult(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        arr = [Node(1, 5), Node(2, 1), Node(3, 5), Node(4, 8)]
        SarbazGhul.countingSortAndPrintResult(arr)
        self.assertEqual("2 1 3 4 ",capturedOutput.getvalue())

