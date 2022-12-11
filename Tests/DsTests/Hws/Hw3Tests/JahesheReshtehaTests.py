# be name khoda
import io
import sys
import unittest
from DsHws.Hw3 import JahesheReshteha
m = 1024
p = 37


class JahesheReshtehaTests(unittest.TestCase):
    def test_calculateHashSuffixesDiffers(self):
        str = "ABCDEFG"
        p = 37
        m = 1024
        suffixes = JahesheReshteha.calculateHashSuffixes(str)
        p_m1 = (ord('A') * p) % m
        self.assertEqual(suffixes[0], p_m1)
        p_m1 += (ord('B') * (p ** 2)) % m
        self.assertEqual(suffixes[1], p_m1)
        p_m1 += (ord('C') * ( p ** 3 )) % m
        self.assertEqual(suffixes[2], p_m1)
        self.assertEqual(suffixes[2] - suffixes[0] , p_m1 - ((ord('A') * p) % m))

    def test_createIntervalTree(self):
        str = "ABCDEFG"
        p = 37
        m = 1024
        suffixes = JahesheReshteha.calculateHashSuffixes(str)
        nodes = []
        JahesheReshteha.createTree(suffixes, 0, len(str), nodes, 0)
        self.assertEqual(nodes[len(nodes) - 1].value, suffixes[3])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.value, suffixes[5] - suffixes[3])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.rightChildren.value, suffixes[6] - suffixes[5])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.leftChildren.value, suffixes[4] - suffixes[5])
        self.assertEqual(nodes[len(nodes) - 1].leftChildren.leftChildren.value, suffixes[0] - suffixes[1])

    def test_createIntervalTree2(self):
        str = "ABCDEFGH"
        str2 = ""
        p = 37
        m = 1024
        suffixes = JahesheReshteha.calculateHashSuffixes(str)
        nodes = []
        JahesheReshteha.createTree(suffixes, 0, len(str) , nodes, 0)
        self.assertEqual(nodes[len(nodes) - 1].value, suffixes[4])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.value, suffixes[6] - suffixes[4])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.rightChildren.value, suffixes[7] - suffixes[6])
        self.assertEqual(nodes[len(nodes) - 1].rightChildren.leftChildren.value, suffixes[5] - suffixes[6])
        self.assertEqual(nodes[len(nodes) - 1].leftChildren.leftChildren.value, suffixes[0] - suffixes[1])


    def test_createHashOfSubString(self):
        str = "GaiusA"
        str2 = "Gaius"
        p = 37
        m = 1024
        suffixes = JahesheReshteha.calculateHashSuffixes(str)
        suffixes2 = JahesheReshteha.calculateHashSuffixes(str2)
        nodes = []
        nodes2 = []
        JahesheReshteha.createTree(suffixes, 0, len(str) - 1, nodes, 0)
        JahesheReshteha.createTree(suffixes2, 0, len(str2) - 1, nodes2, 0)
        self.assertEqual(JahesheReshteha.calculateHashOfSubString(nodes2,0,4) , JahesheReshteha.calculateHashOfSubString(nodes,0,4))

    def test_compareTwoSubstring(self):
        str1 = "ABCDEFG"
        str2 = "BAABCDEFG"
        p = 37
        m = 1024
        hash = p * ( ord('B') * p  + ord('C') * (p ** 2) + ord('D') * (p ** 3) )
        print(hash % m)
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        suffixes2 = JahesheReshteha.calculateHashSuffixes(str2)
        nodes1 = []
        nodes2 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1), nodes1, 0)
        JahesheReshteha.createTree(suffixes2, 0, len(str2), nodes2, 0)
        isEqual = JahesheReshteha.compareTwoSubString(p,m,nodes1,nodes2,1,3,5)
        isEqual2 = JahesheReshteha.compareTwoSubString(p,m,nodes1,nodes2,0,2,5)
        self.assertEqual(isEqual,"YES")
        self.assertEqual(isEqual2,"YES")

    def test_compareTwoSubstring2(self):
        str1 = "GaiusBrutus"
        str2 = "BrutusCaesarGaius"
        p = 37
        m = 1024
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        suffixes2 = JahesheReshteha.calculateHashSuffixes(str2)
        nodes1 = []
        nodes2 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1), nodes1, 0)
        JahesheReshteha.createTree(suffixes2, 0, len(str2), nodes2, 0)
        isEqual = JahesheReshteha.compareTwoSubString(p, m, nodes1, nodes2, 0, 12, 5)
        self.assertEqual(isEqual, "YES")

    def test_changeCharacteres(self):
        str1 = "GaiusBrutus"
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        nodes1 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1), nodes1, 0)
        JahesheReshteha.changeCharacter(nodes1,0,ord('A') - ord(str1[0]))
        self.assertEqual((suffixes1[0] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],0))
        self.assertEqual((suffixes1[1] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],1))
        self.assertEqual((suffixes1[2] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],2))
        self.assertEqual((suffixes1[3] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],3))
        self.assertEqual((suffixes1[4] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],4))
        self.assertEqual((suffixes1[5] +  ord('A') - ord(str1[0])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],5))

    def test_changeCharacteres2(self):
        str1 = "Gaiuajfelijf;aijeoijoj;oaeij;oaofja;ijf;fj;lzkj;lkzj;lkedj;zijsBrutus"
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        nodes1 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1), nodes1, 0)
        JahesheReshteha.changeCharacter(nodes1,2,ord('C') - ord(str1[2]))
        for i in range(0,2) :
            self.assertEqual((suffixes1[i]) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],i))
        for i in range(3,len(nodes1)) :
            self.assertEqual((suffixes1[i] +  ord('C') - ord(str1[2])) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],i))

    def test_changeCharacteres3(self):
        str1 = "Gaiuajfelijf;aijeoijoj;oaeij;oaofja;ijf;fj;lzkj;lkzj;lkedj;zijsBrutus"
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        nodes1 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1), nodes1, 0)
        JahesheReshteha.changeCharacter(nodes1,8,((p ** 9) % m) * (ord('C') - ord(str1[8]))% m)
        for i in range(0,8) :
            self.assertEqual((suffixes1[i]) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],i))
        for i in range(9,len(nodes1)) :
            self.assertEqual((suffixes1[i] + ((p ** 9) % m) * (ord('C') - ord(str1[8]))% m) % 1024 ,JahesheReshteha.calculateSuffixOfIndex(nodes1,0,nodes1[len(nodes1) - 1],i))

    def test_printResult(self):
        capturedValue = io.StringIO()
        sys.stdout = capturedValue
        strings = ["GaiusBrutus", "BrutusCaesarGaius"]
        operations = []
        operations.append("0 1 2 1 13 5")
        operations.append("0 1 2 6 8 6")
        operations.append("1 1 6 C")
        operations.append("0 1 2 6 1 6")
        operations.append("1 2 1 C")
        operations.append("0 1 2 6 1 6")
        operations.append("0 1 2 4 5 2")
        JahesheReshteha.printResult(strings,operations)
        self.assertEqual("YES\nNO\nNO\nYES\nYES\n",capturedValue.getvalue())

    def test_bug(self):
        capturedValue = io.StringIO()
        sys.stdout = capturedValue
        str1 = "GaiusBrutus"
        str2 = "GGaiusBrutus"
        suffixes1 = JahesheReshteha.calculateHashSuffixes(str1)
        suffixes2 = JahesheReshteha.calculateHashSuffixes(str2)
        nodes = []
        nodes2 = []
        JahesheReshteha.createTree(suffixes1, 0, len(str1) - 1, nodes, 0)
        JahesheReshteha.createTree(suffixes2, 0, len(str2) - 1, nodes2, 0)
        JahesheReshteha.changeCharacter(nodes,0,p * (ord('C') - 1))
        self.printString(nodes2)
        JahesheReshteha.changeCharacter(nodes2,1,ord('C') - 1)
        print(JahesheReshteha.compareTwoSubString(p,m,nodes,nodes2,0,1,5))
        self.assertEqual("YES\n", capturedValue.getvalue())

    def printString(self,nodes):
        str = []
        for i in range(-1, len(nodes) - 1) :
            print(chr(JahesheReshteha.calculateHashOfSubString(nodes,i , i + 1)) , end="")
        print("")








