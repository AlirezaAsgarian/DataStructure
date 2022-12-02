import io
import sys
import unittest
import Training.safa
from collections import deque


class safa_tests(unittest.TestCase):
    def test_safa(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        q = deque()
        q.append("1 5")
        q.append("1 17")
        q.append("2 1 1")
        q.append("1 1")
        q.append("2 2 3")
        q.append("2 1 2")
        Training.safa.print_result(2, len(q), q)
        self.assertEqual("5\n23\n18\n", capturedOutput.getvalue())
