


import unittest
from DsHws.TheoryHws.Hw2 import Q6StackWithFindMinAndFindMax

class stackWithFindMinAndFindMax(unittest.TestCase) :
    def test_pushAndPop(self):
        stack = Q6StackWithFindMinAndFindMax.createStack()
        stack.push(5)
        self.assertEqual(stack.pop() , 5)
        stack.push(5)
        stack.push(6)
        self.assertEqual(stack.pop(), 6)
        self.assertEqual(stack.pop() , 5)

    def test_findMax(self):
        stack = Q6StackWithFindMinAndFindMax.createStack()
        stack.push(5)
        self.assertEqual(stack.findMax() , 5)
        stack.push(5)
        stack.push(6)
        stack.push(4)
        stack.push(7)
        stack.push(5)
        self.assertEqual(stack.findMax(), 7)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.findMax() , 7)
        self.assertEqual(stack.pop() , 7)
        self.assertEqual(stack.findMax() , 6)

    def test_findMin(self):
        stack = Q6StackWithFindMinAndFindMax.createStack()
        stack.push(5)
        self.assertEqual(stack.findMin(), 5)
        stack.push(5)
        stack.push(6)
        stack.push(4)
        stack.push(7)
        stack.push(5)
        self.assertEqual(stack.findMin(),4)
        self.assertEqual(stack.pop(), 5)
        self.assertEqual(stack.findMin(), 4)
        self.assertEqual(stack.pop(), 7)
        self.assertEqual(stack.findMin(), 4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.findMin(), 5)
