import unittest
import main


class main_test(unittest.TestCase):
    def test_first_last_name(self):
        result = main.print_hi("aaa")
        self.assertEqual(result, "Ali")

    def test_first_last_middle_name(self):
        result = [4,3,55,6]
        newList = list(result)
        newList.sort()
        resultList = main.merge_sort(result)
        for i in range(len(result)) :
            self.assertEqual(resultList[i],newList[i])

