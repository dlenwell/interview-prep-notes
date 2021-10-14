"""
Memoization Grid Travel Example

Say that you are a traveler on a 2D grid. You begin in the top-left corner and
your goal is to travel to the bottom-right corner. You may only move down or
right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

Write a function gridTraveler(h, w) that calculates this.

example:
> gridTraveler(1, 1) --> 0

if either both inputs are 1 the output is 0

> gridTraveler(1, 0) --> 0

if either input is 0 the output is 0

> gridTraveler(2, 3) --> 3

.---.---.---.
| S |   |   |
:---+---+---:
|   |   | E |
'---'---'---'

1: right, right, down
.---.---.---.
| > | > | v |
:---+---+---:
|   |   | E |
'---'---'---'

2: right, down, right
.---.---.---.
| > | v |   |
:---+---+---:
|   | > | E |
'---'---'---'

3: down, right, right
.---.---.---.
| v |   |   |
:---+---+---:
| > | > | E |
'---'---'---'



"""
import time
import sys


def grid_traveler_memo(height, width, memo={}):
    """
    Memoized traveler
    """
    key = "{},{}".format(height, width)
    reverse_key = "{},{}".format(width, height)

    # because the reverse of the inputs does not effect the results its okay
    # to use the reverse of the key as well.
    if key in memo.keys():
        return(memo[key])
    if reverse_key in memo.keys():
        return(memo[reverse_key])

    if key in memo.keys():
        return(memo[key])
    if height == 1 and width == 1:
        return(1)
    if height == 0 or width == 0:
        return(0)

    memo[key] = grid_traveler_memo(height - 1, width, memo) + \
        grid_traveler_memo(height, width - 1, memo)

    return(memo[key])


def grid_traveler_rec(height, width):
    """
    Recursive traveler
    """
    if height == 1 and width == 1:
        return(1)
    if height == 0 or width == 0:
        return(0)

    return(
        grid_traveler_rec(height - 1, width) +
        grid_traveler_rec(height, width - 1)
    )


def race(height, width):
    """
    This function races the memoized function against straight up recursion.
    """
    print("Memoized function vs recursion:")
    print()
    print("running grid_traveler_memo with height:{} width:{}"
          .format(height, width))

    # with memoization
    start = time.time()
    print(
        "grid_traveler_memo({}, {}) -> {}".format(
            height,
            width,
            grid_traveler_memo(height, width)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))

    print()
    print("----------------------------------------------------------------")
    print()

    # recursion
    print("running grid_traveler_rec with height:{} width:{}"
          .format(height, width))

    start = time.time()
    print(
        "grid_traveler_rec({}, {}) -> {}".format(
            height,
            width,
            grid_traveler_rec(height, width)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


if __name__ == "__main__":
    """
    main program
    """
    try:
        height = int(sys.argv[1])
        width = int(sys.argv[2])
    except IndexError:
        height = 10
        width = 10

    race(height, width)
