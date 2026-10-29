"""
test case for number of islands
"""
from unittest import TestCase

from solution import Solution
from inputs import scenarios

class TestNumberOfIslands(TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_num_islands_bfs(self):
        """
        test for bfs version of solution
        """
        for scenario in scenarios:
            with self.subTest(name=scenario["name"]):
                grid = [row.copy() for row in scenario["grid"]]

                actual = self.solution.numIslandsBFS(grid)

                self.assertIsInstance(actual, int)
                self.assertEqual(actual, scenario["expected"])

    def test_num_islands_dfs(self):
        """
            test for bfs version of solution
        """
        for scenario in scenarios:
            with self.subTest(name=scenario["name"]):
                grid = [row.copy() for row in scenario["grid"]]

                actual = self.solution.numIslandsDFS(grid)

                self.assertIsInstance(actual, int)
                self.assertEqual(actual, scenario["expected"])

