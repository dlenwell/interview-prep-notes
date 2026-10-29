"""
leedcode problem: 
    https://leetcode.com/problems/number-of-islands/description/

Given an m x n 2D binary grid grid which represents a map of '1's (land) 
and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands 
horizontally or vertically. You may assume all four edges of the grid are all 
surrounded by water.

{
        "name": "single island",
        "grid": [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"]
        ],
        "expected": 1
    },

"""
from collections import deque

from inputs import scenarios


class Solution:
    """
    solution class
    """
    def numIslandsBFS(self, grid: list[list[str]]) -> int:
        """
        numIslandsBFS bredth first solution, O(m × n) and uses a memory
        queue to overcome the recursion issue of the dfs version.

        Parameters:
        grid (list): grid is a list of lists as many colums and 
                        rows as you like, 1 is land 0 is water.
        
        Returns:
        int:Returning
        """
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        columns = len(grid[0])
        island_count = 0
        # Define the 4 cardinal directions: (row_offset, column_offset)
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        # Use a queue to track cells that need their neighbors explored
        def sink_island_bfs(start_row: int, start_column: int) -> None:
            memory = deque([(start_row, start_column)])

            # Mark the starting cell as visited immediately by turning it to water
            grid[start_row][start_column] = '0'

            while memory:
                this_row, this_column = memory.popleft()

                for offset_r, offset_c in directions:
                    neighbor_r = this_row + offset_r
                    neighbor_c = this_column + offset_c

                    # Boundary Check, Is the neighbor inside the grid?
                    is_inside_grid = (
                        0 <= neighbor_r < rows
                        and 0 <= neighbor_c < columns
                    )

                    if is_inside_grid:
                        # Land Check, Is the neighbor unvisited land?
                        
                        if grid[neighbor_r][neighbor_c] == '1':
                            # Mark it as water immediately so no other cell re-adds it
                            grid[neighbor_r][neighbor_c] = '0'
                            memory.append((neighbor_r, neighbor_c))

        # Main loop, Scan every single cell in the grid till 
        # we encounter the first land block
        for row in range(rows):
            for column in range(columns):
                if grid[row][column] == '1':
                    island_count += 1
                    # Expand outward layer-by-layer without using recursion
                    sink_island_bfs(row, column)

        return island_count

    def numIslandsDFS(self, grid: list[list[str]]) -> int:
        """
        numIslandsDFS Depth first solution, O(m × n) but DOES 
        break on larger grids because of python recursion limits.

        Parameters:
        grid (list): grid is a list of lists as many colums and 
                     rows as you like, 1 is land 0 is water. 
        
        Returns:
        int:Returning
        """
        if not grid or not grid[0]:
            return 0

        total_rows = len(grid)
        total_columns = len(grid[0])
        island_count = 0

        def sink_island(row_index: int, column_index: int) -> None:
            # Boundary Check, Ensure the coordinates are inside the grid
            is_outside_grid = (
                row_index < 0
                or row_index >= total_rows
                or column_index < 0
                or column_index >= total_columns
            )
            if is_outside_grid:
                return

            # Land Check, If it is water ('0'), there is nothing to explore
            is_water = (grid[row_index][column_index] == '0')
            if is_water:
                return

            # Mark Visited, Convert land to water to prevent re-visiting
            grid[row_index][column_index] = '0'

            # Neighbor Exploration, Recursively explore all 4 cardinal directions
            sink_island(row_index + 1, column_index)  # Look Down
            sink_island(row_index - 1, column_index)  # Look Up
            sink_island(row_index, column_index + 1)  # Look Right
            sink_island(row_index, column_index - 1)  # Look Left

        # Main loop, Scan every single cell in the grid
        for row in range(total_rows):
            for column in range(total_columns):
                # When we find unvisited land, it marks the discovery of a new island
                if grid[row][column] == '1':
                    island_count += 1
                    # sink the newly discovered island using DFS recursion
                    sink_island(row, column)

        return island_count

def main():
    """
    main exercise run through...
    """
    solution = Solution()

    print()
    print("===================================")
    print()
    print("Running scenarios:")
    
    for scenario in scenarios:
        
        print("name: ", scenario["name"])
        actual = solution.numIslandsBFS(scenario["grid"])
        print("result: ", actual)
        if scenario["expected"] == actual:
            print("PASSED!")
        else:
            print("FAILED!")

        print()
        print("===================================")

if __name__ == "__main__":
    """
    triggered when file is executed, ignored when included
    """
    main()