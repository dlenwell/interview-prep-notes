"""
    best Sum

    Write a function `bestSum(target, numbers)` that takes in a target sum and
    an array of numbers as arguments.

    The function dhould return an array containing the shortest combination of
    numbers that add up to exactly the target.

    If there is a tie for the shortest combination , you may return any one
    of the shortest combinations.


    Example:

    bestSum(7, [5, 3, 4, 7]) -> [7]

    bestSum(8, [2, 3, 4, 7]) -> [2, 2, 4]

    bestSum(7, [5, 6]) -> None

    bestSum(0, [1, 2, 3]) -> []

    Complexity:

    recursive time: 0(n^m * m)
    recursive space: 0(m^2)

    memoized time: 0(n*m^2)
    space: 0(m^2)


"""
import time
import sys


def bestSumRec(target, numbers):
    """
        recursive version of the call
    """
    if target == 0:
        return([])
    if target < 0:
        return(None)
    if target in numbers:
        return([target])

    shortest = None

    for number in numbers:
        remainder = target - number
        result = bestSumRec(remainder, numbers)

        if result is not None:
            result.append(number)

            if shortest is None or len(shortest) > len(result):
                shortest = result

    return(shortest)


def bestSumMemo(target, numbers, memo = {}):
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

    shortest = None

    for number in numbers:
        remainder = target - number
        memo[target] = bestSumMemo(remainder, numbers, memo)

        if memo[target] is not None:
            memo[target].append(number)

            if shortest is None or len(shortest) > len(memo[target]):
                shortest = memo[target]

    return(shortest)


def race(target, numbers):
    """
        race
    """
    print("running bestSumMemo with target:{} numbers:{} using memoization..."
          .format(target, numbers))

    # with memoization
    start = time.time()
    print(
        "bestSumMemo({}, {}) -> {}".format(
            target,
            numbers,
            bestSumMemo(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))


    print()
    print()

    # recursion
    print("running bestSumRec with target:{} numbers:{} using recursion..."
          .format(target, numbers))

    start = time.time()
    print(
        "bestSumRec({}, {}) -> {}".format(
            target,
            numbers,
            bestSumRec(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


if __name__ == "__main__":
    """
        triggers race when running from command line
    """
    race(100, [25, 3, 12, 4])
