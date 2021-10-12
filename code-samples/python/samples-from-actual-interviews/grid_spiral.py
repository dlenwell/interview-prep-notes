"""
Grid Spiral question.

write a function that will traverse the grid in a spiral path starting at the
top left and moving right till the edge.
"""
import unittest

grids = {
    1: {
        'grid': [[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]],
        'expected': [1, 2, 3, 6, 9, 8, 7, 4, 5]
    },
    2: {
        'grid': [[1, 2, 3, 4],
                 [5, 6, 7, 8],
                 [9, 10, 11, 12],
                 [13, 14, 15, 16]],
        'expected': [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
    },
    3: {
        'grid': [[1, 2, 3, 4, 5],
                 [6, 7, 8, 9, 10],
                 [11, 12, 13, 14, 15],
                 [15, 16, 17, 18, 19],
                 [20, 21, 22, 23, 24]],
        'expected': [1, 2, 3, 4, 5, 10, 15, 19, 24, 23, 22, 21, 20,
                     15, 11, 6, 7, 8, 9, 14, 18, 17, 16, 12, 13]
    }
}


def add(a, b):
    """
    adds tuple values and maintains tuple
    """
    return((a[0] + b[0], a[1] + b[1]))


def out(grid, position):
    """
    returns boolean indicating if the position is out of bounds.
    """
    # catches right and lower boundries
    try:
        int(grid[position[0]][position[1]])
    except IndexError:
        return(True)

    # catches left and top boundies
    if position[0] < 0:
        return(True)

    if position[1] < 0:
        return(True)

    return(False)


def grid_size(grid):
    """
    returns total node count.. used to determine if the run is finished
    """
    count = 0

    for line in grid:
        count += len(line)

    return(count)


def pivot(direction):
    """
    pivots direction
    0: right, 1: down, 2: left, 3: up
    """
    direction += 1

    # if it hits 4 reset to 0
    if direction == 4:
        direction = 0

    # directions = ['right', 'down', 'left', 'up']
    # print("direction: ", directions[direction])
    return(direction)


def spiral(grid):
    """
    iterative traversal of grid in spiral patern
    """
    visited = {}
    size = grid_size(grid)

    # 0: right, 1: down, 2: left, 3: up
    helper = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    direction = 0

    # start it off at (0, 0)
    position = (0, 0)

    while len(visited) < size:
        # visit
        if str(position) not in visited.keys():
            # add to visited object
            visited[str(position)] = grid[position[0]][position[1]]

            # decide on next position
            next_position = add(position, helper[direction])

            # make sure the new position isnt already visited and is in bounds
            if str(next_position) in visited.keys() or \
                    out(grid, next_position):

                # time to pivot
                direction = pivot(direction)

                # recalculate next_position based on new direction
                next_position = add(position, helper[direction])

            # update position for next run
            position = next_position

    # returns only the values of the dict concated
    return(list(visited.values()))


def functional_test():
    """
    test function I ran while coding the thing
    """
    print("Expected results: ", grids[1]['expected'])
    print("output: ", spiral(grids[1]['grid']))
    print()
    print("Expected results: ", grids[2]['expected'])
    print("output: ", spiral(grids[2]['grid']))
    print()
    print("Expected results: ", grids[3]['expected'])
    print("output: ", spiral(grids[3]['grid']))


class TestSpiral(unittest.TestCase):
    """
    tests if results match expected results
    """
    def test_spiral(self):
        for id in grids.keys():
            self.assertListEqual(
                spiral(grids[id]['grid']),
                grids[id]['expected']
            )


if __name__ == '__main__':
    unittest.main()
