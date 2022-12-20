import io
import sys
import unittest
from DsHws.Hw3 import JaheshReshtehaWithSegmentTree

m = 10 ** 9 + 7

class segmentTreeTests(unittest.TestCase):
    def test_createTree(self):
        str = ['A', 'B', 'C', 'D']
        nodes = JaheshReshtehaWithSegmentTree.createNodes(str)
        segmentTree = JaheshReshtehaWithSegmentTree.createTree(nodes, list(nodes))
        self.assertEqual(segmentTree[len(segmentTree) - 1].value , ord('A') + ord('B') + ord('C') + ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].low, 0)
        self.assertEqual(segmentTree[len(segmentTree) - 1].high, 3)
        self.assertEqual(segmentTree[len(segmentTree) - 1].rightChildren.value, ord('C') + ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.value, ord('A') + ord('B'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.value, ord('A'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.value, ord('B'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].rightChildren.rightChildren.value, ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].rightChildren.leftChildren.value, ord('C'))

    def test_createTree2(self):
        str = ['A', 'B', 'C', 'D', 'H']
        nodes = JaheshReshtehaWithSegmentTree.createNodes(str)
        segmentTree = JaheshReshtehaWithSegmentTree.createTree(nodes, list(nodes))
        self.assertEqual(segmentTree[len(segmentTree) - 1].value, ord('A') + ord('B') + ord('C') + ord('D') + ord('H'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].rightChildren.value, ord('H'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.value,
                         ord('A') + ord('B') + ord('C') + ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.low, 0)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.value, ord('A') + ord('B'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.low, 0)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.high, 1)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.value, ord('C') + ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.low, 2)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.high, 3)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.rightChildren.value, ord('D'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.leftChildren.value, ord('C'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.rightChildren.leftChildren.low, 2)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.rightChildren.value, ord('B'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.rightChildren.low, 1)
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.leftChildren.value, ord('A'))
        self.assertEqual(segmentTree[len(segmentTree) - 1].leftChildren.leftChildren.leftChildren.low, 0)

    def test_queryOnSumOfSubString(self):
        str = ['A', 'B', 'C', 'D', 'H']
        nodes = JaheshReshtehaWithSegmentTree.createNodes(str)
        segmentTree = JaheshReshtehaWithSegmentTree.createTree(nodes, list(nodes))
        sum = JaheshReshtehaWithSegmentTree.query(2, 2 + 3 - 1, nodes[len(nodes) - 1])
        self.assertEqual(sum, ord('C') + ord('D') + ord('H'))

    def test_updateTree(self):
        str = ['A', 'B', 'C', 'D', 'H']
        nodes = JaheshReshtehaWithSegmentTree.createNodes(str)
        segmentTree = JaheshReshtehaWithSegmentTree.createTree(nodes, list(nodes))
        JaheshReshtehaWithSegmentTree.updateTree(nodes[len(nodes) - 1],3, ord(str[3]), ord('Q'))
        testQuery = JaheshReshtehaWithSegmentTree.query(1, 1 + 3 - 1, nodes[len(nodes) - 1])
        self.assertEqual(ord('B') + ord('C') + ord('Q'), testQuery)

    def test_compareToSubString(self):
        str1 = "ABCDFQ"
        str2 = "FFABCDFG"
        nodes1 = JaheshReshtehaWithSegmentTree.createNodes(str1)
        nodes2 = JaheshReshtehaWithSegmentTree.createNodes(str2)
        JaheshReshtehaWithSegmentTree.createTree(nodes1,list(nodes1))
        JaheshReshtehaWithSegmentTree.createTree(nodes2,list(nodes2))
        isEqual = JaheshReshtehaWithSegmentTree.compareTwoString(nodes1,nodes2,1,3,5)
        self.assertEqual("YES",isEqual)
        JaheshReshtehaWithSegmentTree.updateTree(nodes1[len(nodes1) - 1],6 - 1,ord(str1[6 - 1]),ord('C'))
        JaheshReshtehaWithSegmentTree.updateTree(nodes2[len(nodes2) - 1],8 - 1,ord(str2[8 - 1]),ord('C'))
        isEqual2 = JaheshReshtehaWithSegmentTree.compareTwoString(nodes1,nodes2,1,3,6)
        self.assertEqual("YES",isEqual2)

    def test_compareTwoSubString2AndUpdateTree(self):
        str1 = "GaiusBrutus"
        str2 = "BrutusCaesarGaius"
        nodes1 = JaheshReshtehaWithSegmentTree.createNodes(str1)
        nodes2 = JaheshReshtehaWithSegmentTree.createNodes(str2)
        JaheshReshtehaWithSegmentTree.createTree(nodes1,list(nodes1))
        JaheshReshtehaWithSegmentTree.createTree(nodes2,list(nodes2))
        isEqual = JaheshReshtehaWithSegmentTree.compareTwoString(nodes1,nodes2,1,13,5)
        self.assertEqual("YES",isEqual)
        JaheshReshtehaWithSegmentTree.updateTree(nodes1[len(nodes1) - 1],6 - 1,ord(str1[6 - 1]),ord('C'))
        JaheshReshtehaWithSegmentTree.updateTree(nodes2[len(nodes2) - 1],1 - 1,ord(str2[1 - 1]),ord('C'))
        isEqual2 = JaheshReshtehaWithSegmentTree.compareTwoString(nodes1,nodes2,6,1,6)
        self.assertEqual("YES",isEqual2)

    def test_printResult(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        strings = ["GaiusBrutus","BrutusCaesarGaius"]
        operations = ["0 1 2 1 13 5","0 1 2 6 8 6","1 1 6 C","0 1 2 6 1 6","1 2 1 C","0 1 2 6 1 6","0 1 2 4 5 2"]
        JaheshReshtehaWithSegmentTree.printResult(strings,operations)
        self.assertEqual("YES\nNO\nNO\nYES\nYES\n",capturedOutput.getvalue())




