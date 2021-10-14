#!/usr/bin/env python3
"""
tests for quicksort
"""
import unittest
from util import generate_criteria
from quicksort import quick_sort_iterative, quick_sort_recursive

criteria = {}


class TestQuickSort(unittest.TestCase):
    """
    tests if results match expected results
    """

    def test_quick_sort_recursive(self):
        """
        Test the recurisve version of quick sort with lists that are 50, 500
        and 1000 items in length.

        it will fail when it tries to sort the large list because of pythons
        built in recursion limit.
        """
        for size in criteria.keys():
            self.assertListEqual(
                quick_sort_recursive(criteria[size]['list']),
                criteria[size]['expect']
            )

    def test_quick_sort_iterative(self):
        """
        Test the recurisve version of quick sort with lists that are 50, 500
        and 1000 items in length.

        The iterative version of the function won't fail in that instance
        because it doesn't rely on recursion.
        """
        for size in criteria.keys():
            self.assertListEqual(
                quick_sort_iterative(criteria[size]['list']),
                criteria[size]['expect']
            )


if __name__ == '__main__':
    """
    calling this script from the console will trigger the unit tests.
    """
    # generate test criteria before running tests
    criteria = generate_criteria({
        50: {},
        500: {},
        1000: {}
    })

    # trigger unit test
    unittest.main()
