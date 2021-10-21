"""
tests for sliding window examples
"""
from unittest import main, TestCase
from sliding_window import max_sum, shortest_larger_than
from strings import min_sub_string, longest_sub_string, longest_consecutive


class TestLongestConsecutive(TestCase):

    scenerios = [
        {
            'data': "ABBCCCDDDDEEEEFFFFFFF",
            'assert': 7
        },
        {
            'data': "ABBCCCDDDDEEEEEFF",
            'assert': 5
        },
    ]

    def test_longest_consecutive(self):
        """
        test for longest_consecutive
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                longest_consecutive(scenerio['data']),
                scenerio['assert']
            )


class TestLongestSubString(TestCase):

    scenerios = [
        {
            'data': "WEREWSDESSEDTEEWSSE",
            'assert': 6
        },
        {
            'data': "WEWERWERWERWEDJJDMUSHHENREWSDESSEDTEEWSS",
            'assert': 11
        },
    ]

    def test_longest_sub_string(self):
        """
        test for longest_sub_string
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                longest_sub_string(scenerio['data']),
                scenerio['assert']
            )


class TestMinSubString(TestCase):

    scenerios = [
        {
            'haystack': "this is a string",
            'needles': "hn",
            'assert': "his is a strin"
        },
        {
            'haystack': "ABDEFRESCE",
            'needles': "ABC",
            'assert': "ABDEFRESC"
        },
        {
            'haystack': "ABDEFRESCE",
            'needles': "AWC",
            'assert': None
        },
    ]

    def test_min_sub_string(self):
        """
        test for min_sub_string
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                min_sub_string(scenerio['haystack'], scenerio['needles']),
                scenerio['assert']
            )


class TestMaxSum(TestCase):

    scenerios = [
        {
            'length': 3,
            'sequence': [4, 3, 1, 2, 3, 5, 3, 2, 8],
            'assert': 13
        },
        {
            'length': 4,
            'sequence': [4, 3, 1, 5, 3, 5, 3, 2, 8],
            'assert': 18
        },
    ]

    def test_max_sum(self):
        """
        test for max_sum
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                max_sum(scenerio['sequence'], scenerio['length']),
                scenerio['assert']
            )


class TestShortestLargerThan(TestCase):

    scenerios = [
        {
            'max': 12,
            'sequence': [4, 3, 1, 2, 3, 5, 3, 2, 8],
            'assert': 3
        },
        {
            'max': 15,
            'sequence': [4, 3, 1, 5, 3, 5, 3, 2, 8],
            'assert': 4
        },
    ]

    def test_shortest_larger_than(self):
        """
        test for shortest_larger_than
        """
        for scenerio in self.scenerios:
            self.assertEqual(
                shortest_larger_than(scenerio['sequence'], scenerio['max']),
                scenerio['assert']
            )


if __name__ == '__main__':
    main()
