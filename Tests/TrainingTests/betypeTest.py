import io
import sys
import unittest
import Training.betype



class betype_tests(unittest.TestCase):
    def test_beType(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Training.betype.getResult("sall=am")
        self.assertEqual("salam",capturedOutput.getvalue())

    def test_beType(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Training.betype.getResult("=sall=am")
        self.assertEqual("salam", capturedOutput.getvalue())
