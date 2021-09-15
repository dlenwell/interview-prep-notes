"""
    can Sum

    Write a function `canSum(target, numbers)` that takesin a target and an an
    array of number as arguments.

    The function should return a boolean indicating whater or not is possible to
    generate the targetSum using numbers from the array.

    Restraints:
    - You may use an element of the array as manu times as needed.
    - You may assume that all input numbers are nonnegative.


    target case:
    > canSum(7, [5, 3, 4, 7]) --> True

    > canSum(7, [2, 4]) --> False

"""
import time
import sys


def canSumRec(target, numbers):
    """
        Recursive version of the call
    """
    if target in numbers:
        return(True)
    if target is 0:
        return(True)
    if target < 0:
        return(False)

    for number in numbers:
        remainder = target - number

        if canSumRec(remainder, numbers) is True:
            return True

    return False


def canSumMemo(target, numbers, memo = {}):
    """
        Memoized version of the function
    """
    if target in memo.keys():
        return(memo[target])
    if target in numbers:
        return(True)
    if target is 0:
        return(True)
    if target < 0:
        return(False)

    for number in numbers:
        remainder = target - number
        memo[target] = canSumMemo(remainder, numbers, memo)

        return memo[target]

    return False


def race(target, numbers):
    """
        This function times the same inputs against recursive alone and
        recursive with memoization.
    """
    print("running canSumMemo with target:{} numbers:{} using memoization..."
          .format(target, numbers))

    # with memoization
    start = time.time()
    print(
        "canSumMemo({}, {}) -> {}".format(
            target,
            numbers,
            canSumMemo(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))


    print()
    print()

    # recursion
    print("running canSumRec with target:{} numbers:{} using recursion..."
          .format(target, numbers))

    start = time.time()
    print(
        "canSumRec({}, {}) -> {}".format(
            target,
            numbers,
            canSumRec(target, numbers)
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
    numbers = [7, 14]
    target = 250

    print("Hi im running a can Sum race.")

    race(target, numbers)

if __name__ == "__main__":
    main()
