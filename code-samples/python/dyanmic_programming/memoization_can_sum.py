"""
can sum

Write a function `can_sum(target, numbers)` that takesin a target and an an
array of number as arguments.

The function should return a boolean indicating whater or not is possible to
generate the targetSum using numbers from the array.

Restraints:
- You may use an element of the array as manu times as needed.
- You may assume that all input numbers are nonnegative.


target case:
> can_sum(7, [5, 3, 4, 7]) --> True

> can_sum(7, [2, 4]) --> False

"""
import time


def can_sum_rec(target, numbers):
    """
    Recursive version of the call
    """
    if target in numbers:
        return(True)
    if target == 0:
        return(True)
    if target < 0:
        return(False)

    for number in numbers:
        remainder = target - number

        if can_sum_rec(remainder, numbers) is True:
            return(True)

    return(False)


def can_sum_memo(target, numbers, memo={}):
    """
    Memoized version of the function
    """
    if target in memo.keys():
        return(memo[target])
    if target in numbers:
        return(True)
    if target == 0:
        return(True)
    if target < 0:
        return(False)

    for number in numbers:
        remainder = target - number
        memo[remainder] = can_sum_memo(remainder, numbers, memo)

        return(memo[remainder])

    return(False)


def race(target, numbers):
    """
    This function times the same inputs against recursive alone and
    recursive with memoization.
    """
    print("running can_sum_memo with target:{} numbers:{}"
          .format(target, numbers))

    start = time.time()
    print(
        "can_sum_memo({}, {}) -> {}".format(
            target,
            numbers,
            can_sum_memo(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))

    print()
    print()

    # recursion
    print("running can_sum_rec with target:{} numbers:{}"
          .format(target, numbers))

    start = time.time()
    print(
        "can_sum_rec({}, {}) -> {}".format(
            target,
            numbers,
            can_sum_rec(target, numbers)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


def manual_test():
    """
    """
    scenerios = [
        {
            'target': 100,
            'numbers': [7, 14],
            'assert': False
        },
        {
            'target': 100,
            'numbers': [25, 7, 34, 14],
            'assert': True
        }
    ]

    for scenerio in scenerios:
        print(
            "can_sum_memo({}, {}) -> ".format(
                scenerio['target'],
                scenerio['numbers']
            ),
            can_sum_memo(scenerio['target'], scenerio['numbers'])
        )


if __name__ == "__main__":
    """
    test code when triggered from the command line.
    """

    manual_test()
