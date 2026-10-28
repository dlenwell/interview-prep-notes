"""
tests
"""
from unittest import TestCase
from solution import Solution

from inputs import scenarios


class TesttopKFrequent(TestCase):

    def setUp(self):
        """Runs before every individual test method to set up clean state."""
        self.solution = Solution()

    def test_topKFrequent(self):
        """
        testing 
        """
        for scenario in scenarios:
            with self.subTest(
                nums=scenario["nums"],
                k=scenario["k"]
            ):
                actual = self.solution.topKFrequentoptimized(scenario["nums"],scenario["k"])
                self.assertIsInstance(actual, list)
                self.assertEqual(
                    actual,
                    scenario["assert"]
                )