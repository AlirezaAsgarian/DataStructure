import unittest
import sys
import io
import Training.masahateMashoor


class masahateMashoorTest(unittest.TestCase):
    def test_first(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sizeOfRectangles = [2, 5, 7, 6, 3, 1]
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("15\n", capturedOutput.getvalue())
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("15\n15\n", capturedOutput.getvalue())

    def test_same_numbers(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sizeOfRectangles = [1, 3, 3, 2, 4, 4, 6, 4]
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("16\n", capturedOutput.getvalue())
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("16\n16\n", capturedOutput.getvalue())

    def test_same_numbers2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sizeOfRectangles = [1, 3, 3, 3, 4, 4, 6, 4]
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("21\n", capturedOutput.getvalue())
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("21\n21\n", capturedOutput.getvalue())

    def test_same_numbers3(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sizeOfRectangles = [2 ,9 ,9 ,9, 8 , 6 , 10, 11 ,13, 9, 7]
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("60\n", capturedOutput.getvalue())
        Training.masahateMashoor.printResult(sizeOfRectangles)
        self.assertEqual("60\n60\n", capturedOutput.getvalue())
