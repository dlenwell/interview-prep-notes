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

    hasSumRec(7, [5, 3, 4, 7]) -> [3, 4]

    hasSumRec(8, [2, 3, 4, 7]) -> [2, 2, 2, 2]

    hasSumRec(7, [5, 6]) -> None

    hasSumRec(0, [1, 2, 3]) -> []

    Complexity:

    recursive time: 0(n^m * m)
    recursive space: 0(m)

    memoized time: 0(n*m^2)
    space: 0(m^2)


"""
import time
import sys


def hasSumRec(target, numbers):
    """
        recursive version of the call
    """
    if target == 0:
        return([])
    if target < 0:
        return(None)
    if target in numbers:
        return([target])

    for number in numbers:
        remainder = target - number
        result = hasSumRec(remainder, numbers)

        if result is not None:
            result.append(number)
            return(result)

    return(None)


def hasSumMemo(target, numbers, memo = {}):
    """
        memoized version of the function
    """
    if target in memo.keys():
        return(memo[target])
    if target == 0:
        return([])
    if target < 0:
        return(None)
    if target in numbers:
        return([target])

    for number in numbers:
        remainder = target - number
        memo[target] = hasSumMemo(remainder, numbers, memo)

        if memo[target] is not None:
            memo[target].append(number)
            return(memo[target])

    memo[target] = None
    return(None)


def race(target, numbers):
    """
        race
    """


def main():
    """
        main program
    """

    print("hi running canSum")
    print("hasSumMemo(300, [7, 14]) -> {}".format(hasSumMemo(300, [7, 14])))
    #print("canSum(300, [7, 14]) -> {}".format(canSumMemo(300, [7, 14])))

    #race(300, [7, 14])

if __name__ == "__main__":
    main()
