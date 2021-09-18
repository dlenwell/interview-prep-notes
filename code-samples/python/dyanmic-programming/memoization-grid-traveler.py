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


def gridTravelerMemo(height, width, memo = {}):
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
    if height is 1 and width is 1:
        return(1)
    if height is 0 or width is 0:
        return(0)

    memo[key] = gridTravelerMemo(height -1, width, memo) + \
        gridTravelerMemo(height, width - 1, memo)

    return(memo[key])


def gridTravelerRec(height, width):
    """
        Recursive traveler

    """
    if height is 1 and width is 1:
        return(1)
    if height is 0 or width is 0:
        return(0)

    return(
        gridTravelerRec(height -1, width) + gridTravelerRec(height, width - 1)
    )


def race(height, width):
    """
    """
    print("running gridTravelerMemo with height:{} width:{} using memoization..."
          .format(height, width))

    # with memoization
    start = time.time()
    print(
        "gridTravelerMemo({}, {}) -> {}".format(
            height,
            width,
            gridTravelerMemo(height, width)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))


    print()
    print()

    # recursion
    print("running gridTravelerRec with height:{} width:{} using recursion..."
          .format(height, width))

    start = time.time()
    print(
        "gridTravelerRec({}, {}) -> {}".format(
            height,
            width,
            gridTravelerRec(height, width)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


def main():
    """
    main program
    """

    print("hi running grid traveller recursive function")

    default_width = 12

    try:
        height = int(sys.argv[1])
    except IndexError:
        height = 12

    try:
        width = int(sys.argv[2])
    except IndexError:
        width = 12

    race(height, width)


if __name__ == "__main__":
    main()
