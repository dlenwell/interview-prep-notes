"""
tests for the binary_search folder
"""
import unittest
from binary_search_integer_list import index_of_iterative, index_of_recursive


class TestBinarySearchIntegerList(unittest.TestCase):

    scenerios = [
        {
            'haystack': [0, 5, 8, 12, 20, 31, 33, 40, 50, 56, 73, 79, 83, 85,
                         94, 101, 108, 115, 118, 153, 159, 160, 161, 172, 175,
                         198, 198, 198, 200, 207, 209, 213, 216, 228, 232, 235,
                         247, 252, 252, 258, 262, 262, 267, 267, 270, 274, 274,
                         282, 287, 292, 303, 310, 314, 318, 329, 332, 337, 342,
                         345, 345, 350, 354, 359, 361, 365, 365, 369, 387, 389,
                         395, 400, 407, 410, 412, 414, 414, 415, 415, 417, 423,
                         430, 431, 433, 434, 445, 449, 450, 453, 455, 457, 460,
                         466, 467, 472, 478, 478, 488, 493, 497],
            'needle': 292,
            'assert': 49
        },
        {
            'haystack': [0, 5, 8, 12, 20, 31, 33, 40, 50, 56, 73, 79, 83, 85,
                         94, 101, 108, 115, 118, 153, 159, 160, 161, 172, 175,
                         198, 198, 198, 200, 207, 209, 213, 216, 228, 232, 235,
                         247, 252, 252, 258, 262, 262, 267, 267, 270, 274, 274,
                         282, 287, 292, 303, 310],
            'needle': 150,
            'assert': None
        }
    ]

    def test_index_of_iterative(self):
        """
        test for index_of_iterative
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                index_of_iterative(scenerio['haystack'], scenerio['needle']),
                scenerio['assert']
            )

    def test_index_of_recursive(self):
        """
        test for index_of_recursive
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                index_of_recursive(scenerio['haystack'], scenerio['needle']),
                scenerio['assert']
            )


def main():
    """
    initiate tests from command line
    """
    unittest.main()


if __name__ == '__main__':
    main()
