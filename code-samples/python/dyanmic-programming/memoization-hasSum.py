"""
    has Sum

    Write a function `howSum(target, numbers)` that takes in targetSum and an
    array of numbers as arguements.

    The function should return an array containing any combination of elements
    that add up exactly to the target. If there is no combination that adds up
    to the target, then return None.

    If there are multple combinations possible, you may return any single one.


    Example:

    hasSumRec(7, [5, 3, 4, 7]) -> [7]

    hasSumRec(7, [5, 6]) -> None

    hasSumRec(0, [1, 2, 3]) -> []



"""
import time
import sys


def hasSumRec(target, numbers):
    """
        recursive version of the call
    """
    


def hasSumMemo(target, numbers, memo = {}):
    """
        memoized version of the function
    """


def race(target, numbers):
    """
        race
    """


def main():
    """
        main program
    """

    print("hi running canSum")

    print("hasSumRec(7, [5, 3, 4, 7]) -> {}".format(hasSumRec(7, [5, 3, 4, 7])))
    #print("canSum(300, [7, 14]) -> {}".format(canSumMemo(300, [7, 14])))


    #race(300, [7, 14])

if __name__ == "__main__":
    main()
