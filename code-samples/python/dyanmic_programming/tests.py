"""
This file contains unit tests for the examples in the dynamic programming
folder.


"""
import unittest
from memoization_best_sum import best_sum_memo
from memoization_can_construct import can_construct_memo
from memoization_can_sum import can_sum_memo


class TestCanSum(unittest.TestCase):
    """
    tests if results match expected results
    """
    scenerios = [
        {
            'target': 100,
            'numbers': [7, 14],
            'assert': False
        },
        {
            'target': 100,
            'numbers': [25, 7, 14],
            'assert': True
        }
    ]

    def test_can_sum(self):
        """
        test for can construct memoized
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                can_sum_memo(scenerio['target'], scenerio['numbers']),
                scenerio['assert']
            )


class TestCanConstruct(unittest.TestCase):
    """
    tests if results match expected results
    """
    scenerios = [
        {
            'target': "abcdef",
            'words': ['ab', 'abc', 'cd', 'def', 'abcd'],
            'assert': True
        },
        {
            'target': "skateboard",
            'words': ['bo', 'rd', 'ate', 't', 'ska', "sk", "boar"],
            'assert': False
        },
        {
            'target': "enterapotentpot",
            'words': ["a", "p", "ent", "enter", "ot", "o", "t"],
            'assert': True
        },
        {
            'target': "running can_construct_rec with target.",
            'words': ["run", "n", "in", "g", "con", " ", "_", "tar",
                      "ge", "t", ".", "c", "a", "struct_rec", "with"],
            'assert': True
        }
    ]

    def test_can_construct_memo(self):
        """
        test for can construct memoized
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                can_construct_memo(scenerio['target'], scenerio['words']),
                scenerio['assert']
            )


class TestBestSum(unittest.TestCase):
    """
    tests if results match expected results
    """
    scenerios = [
        {
            'target': 100,
            'numbers': [7, 14],
            'assert': None
        },
        {
            'target': 100,
            'numbers': [25, 3, 12, 4],
            'assert': [25, 25, 25, 25]
        }
    ]

    def test_best_sum_memo(self):
        """
        test for best sum WITH memoization
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                best_sum_memo(scenerio['target'], scenerio['numbers']),
                scenerio['assert']
            )


if __name__ == '__main__':
    """
    initiate tests from command line
    """
    unittest.main()
