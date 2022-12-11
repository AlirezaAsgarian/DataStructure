import io
import sys
import unittest

from Training.PiadeRow import  *

# 5 3
# 0 1 0 0 1
# 1 3
# 2 4
# 4 5


class PiadeRow_tests(unittest.TestCase) :
    def test_caluclateNumberOfErrors(self):
        nodes = calculateNumberOfErrors([1, 1, 1, 0, 1, 0, 0])
        self.assertEqual(nodes[1].numberOfErrors , 1)
        self.assertEqual(nodes[2].numberOfErrors , 2)
        self.assertEqual(nodes[3].numberOfErrors , 2)
        self.assertEqual(nodes[4].numberOfErrors , 2)
        self.assertEqual(nodes[5].numberOfErrors , 2)
        self.assertEqual(nodes[6].numberOfErrors , 3)

    def test_printResult(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        nodes = calculateNumberOfErrors([0 , 1 , 0 , 0 ,1])
        printError(nodes[0],nodes[2])
        printError(nodes[1],nodes[3])
        printError(nodes[3],nodes[4])
        self.assertEqual("YES\nNO\nYES\n",capturedOutput.getvalue())
