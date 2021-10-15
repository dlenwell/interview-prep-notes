"""
This file contains unit tests for the examples in the dynamic programming
folder.


"""
import unittest
from memoization_best_sum import best_sum_rec, best_sum_memo


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

    def test_best_sum_rec(self):
        """
        test for best sum without memoization
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                best_sum_rec(scenerio['target'], scenerio['numbers']),
                scenerio['assert']
            )

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
    unittest.main()
