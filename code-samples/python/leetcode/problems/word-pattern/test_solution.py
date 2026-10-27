"""
tests for sliding window examples
"""
from unittest import TestCase
from solution import Solution
from inputs import scenarios

class TestWordPattern(TestCase):

    def setUp(self):
        """Runs before every individual test method to set up clean state."""
        self.solution = Solution()

    def test_word_pattern(self):
        """
        testing 
        """
        for scenario in scenarios:
            with self.subTest(
                pattern=scenario["pattern"],
                data=scenario["data"]
            ):
                self.assertEqual(
                    self.solution.wordPattern(
                        scenario["pattern"],
                        scenario["data"]
                    ),
                    scenario["assert"]
                )