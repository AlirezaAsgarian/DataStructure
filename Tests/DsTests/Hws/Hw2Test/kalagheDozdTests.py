import io
import sys
import time
import unittest
import DsHws.Hw2.kalagheDozd


class kalaghe_dozd_test(unittest.TestCase):
    def test_isPrime(self):
        self.assertTrue(DsHws.Hw2.kalagheDozd.isPrime(97))
        self.assertTrue(DsHws.Hw2.kalagheDozd.isPrime(3))
        self.assertFalse(DsHws.Hw2.kalagheDozd.isPrime(4))

    def test_isDivisionOfPowerOfTwo(self):
        self.assertTrue(DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(2,16))
        self.assertFalse(DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(2,8))
        self.assertTrue(DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(3,9))
        self.assertTrue(DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(3,81))
        self.assertFalse(DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(3,27))

    def test_heap(self):
        primes = DsHws.Hw2.kalagheDozd.getPrimeNumbers(100)
        heap = DsHws.Hw2.kalagheDozd.heap(primes)
        self.assertEqual(2,heap.removeMin())
        heap.push(4)
        self.assertEqual(3,heap.removeMin())
        self.assertEqual(4,heap.removeMin())


    def test_getAppropiateNumbers(self):
        appropiateNumbers = DsHws.Hw2.kalagheDozd.getAppropiateNumbers(100)
        self.assertEqual(appropiateNumbers[2],4)
        self.assertEqual(appropiateNumbers[1],3)
        self.assertEqual(appropiateNumbers[5],9)

    def test_getFirstKPrimeNumbers(self):
        primes = DsHws.Hw2.kalagheDozd.getPrimeNumbers(100)
        counter = 0
        for i in primes:
            self.assertTrue(DsHws.Hw2.kalagheDozd.isPrime(i) or DsHws.Hw2.kalagheDozd.isDivisionOfPowerOfTwo(i,))
            counter += 1
        self.assertEqual(counter, 100)

    def test_getResult(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        DsHws.Hw2.kalagheDozd.printResult(4)
        self.assertEqual("120\n", capturedOutput.getvalue())
        DsHws.Hw2.kalagheDozd.printResult(5)
        self.assertEqual("120\n840\n", capturedOutput.getvalue())
        DsHws.Hw2.kalagheDozd.printResult(8)
        self.assertEqual("120\n840\n1081080\n", capturedOutput.getvalue())
        DsHws.Hw2.kalagheDozd.printResult(10)
        self.assertEqual("120\n840\n1081080\n294053760\n", capturedOutput.getvalue())

    def test_getResult2(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        DsHws.Hw2.kalagheDozd.printResult(10)
        self.assertEqual("294053760\n", capturedOutput.getvalue())
        DsHws.Hw2.kalagheDozd.printResult(18)
        self.assertEqual("294053760\n306099001\n", capturedOutput.getvalue())
        DsHws.Hw2.kalagheDozd.printResult(29)
        self.assertEqual("294053760\n306099001\n840835559\n", capturedOutput.getvalue())
        start = time.time()
        DsHws.Hw2.kalagheDozd.printResult(1000000)
        end = time.time()
        self.assertEqual("294053760\n306099001\n840835559\n667294949\n", capturedOutput.getvalue())
        print(end - start)
        self.assertTrue((end - start) < 6000)

    def test_maxInput(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        start = time.time()
        DsHws.Hw2.kalagheDozd.printResult(1000000)
        end = time.time()
        self.assertEqual("667294949\n", capturedOutput.getvalue())
        print(end - start)
        self.assertTrue((end - start) < 6000)


