"""
tests
"""
from unittest import TestCase
from solution import Solution
from inputs import scenarios_no_dup, scenarios_dup, normalize


class TestGroupAnagrams(TestCase):
    def setUp(self):
        """Runs before every individual test method to set up clean state."""
        self.solution = Solution()

    def test_group_anagrams_counter_dup(self):
        """
        testing 
        """
        for scenario in scenarios_dup:
            with self.subTest(
                data=scenario["data"]
            ):
                self.assertEqual(
                    normalize(self.solution.groupAnagramsCounter_preservedup(
                        scenario["data"]
                    )),
                    normalize(scenario["assert"])
                )

    def test_group_anagrams_counter_nodup(self):
            """
            testing 
            """
            for scenario in scenarios_no_dup:
                with self.subTest(
                    data=scenario["data"]
                ):
                    self.assertEqual(
                        normalize(self.solution.groupAnagramsCounter_nodup(
                            scenario["data"]
                        )),
                        normalize(scenario["assert"])
                    )

    def test_group_anagrams_sorted(self):
        """
        testing 
        """
        for scenario in scenarios_no_dup:
            with self.subTest(
                data=scenario["data"]
            ):
                actual = self.solution.groupAnagramsSorted(scenario["data"])
                self.assertIsInstance(actual, list)
                self.assertEqual(
                    normalize(actual),
                    normalize(scenario["assert"])
                )

    def test_group_anagrams_optimized(self):
            """
            testing 
            """
            for scenario in scenarios_dup:
                with self.subTest(
                    data=scenario["data"]
                ):
                    actual = self.solution.groupAnagramsOptimized(scenario["data"])
                    self.assertIsInstance(actual, list)
                    self.assertEqual(
                        normalize(actual),
                        normalize(scenario["assert"])
                    )