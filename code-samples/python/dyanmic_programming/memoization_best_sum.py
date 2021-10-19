"""
memoization_best_sum

Write a function `best_sum(target, numbers)` that takes in a target sum and
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


def best_sum_rec(target, numbers):
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
        result = best_sum_rec(remainder, numbers)

        if result is not None:
            result.append(number)

            if shortest is None or len(shortest) > len(result):
                shortest = result

    return(shortest)


def best_sum_memo(target, numbers, memo={}):
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
        result = best_sum_memo(remainder, numbers, memo)

        if result is not None:
            memo[target] = result + [number]

            if shortest is None or len(shortest) > len(memo[target]):
                shortest = memo[target]

    return(shortest)


def race(target, numbers):
    """
    This function races the memoized function against straight up recursion.
    """
    print("Memoized function vs recursion:")
    print()
    print("running best_sum_memo with target:{} numbers:{} using memoization."
          .format(target, numbers))
    print()
    # with memoization
    start = time.time()
    print(
        "best_sum_memo({}, {}) -> {}".format(
            target,
            numbers,
            best_sum_memo(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))

    print()
    print("----------------------------------------------------------------")
    print()

    # recursion
    print("running best_sum_rec with target:{} numbers:{} using recursion."
          .format(target, numbers))
    print()
    start = time.time()
    print(
        "best_sum_rec({}, {}) -> {}".format(
            target,
            numbers,
            best_sum_rec(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


def manual_test():
    """
    Manually exercise test code for debugging
    """
    scenerios = [
        {
            'target': 100,
            'numbers': [7, 14],
            'assert': None
        },
        {
            'target': 100,
            'numbers': [25, 10],
            'assert': True
        }
    ]

    for scenerio in scenerios:
        print(
            "can_sum_memo({}, {}) -> ".format(
                scenerio['target'],
                scenerio['numbers']
            ),
            best_sum_memo(scenerio['target'], scenerio['numbers'])
        )


if __name__ == "__main__":
    """
    test code when triggered from the command line.
    """

    manual_test()
