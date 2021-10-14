"""
has sum

Write a function `has_sum(target, numbers)` that takes in target and an
array of numbers as arguements.

The function should return an array containing any combination of elements
that add up exactly to the target. If there is no combination that adds up
to the target, then return None.

If there are multple combinations possible, you may return any single one.


Example:

has_sum_rec(7, [5, 3, 4, 7]) -> [7]

has_sum_rec(7, [5, 3, 4, 7]) -> [3, 4]

has_sum_rec(8, [2, 3, 4, 7]) -> [2, 2, 2, 2]

has_sum_rec(7, [5, 6]) -> None

has_sum_rec(0, [1, 2, 3]) -> []

Complexity:

recursive time: 0(n^m * m)
recursive space: 0(m)

memoized time: 0(n*m^2)
space: 0(m^2)

"""


def has_sum_rec(target, numbers):
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
        result = has_sum_rec(remainder, numbers)

        if result is not None:
            result.append(number)
            return(result)

    return(None)


def has_sum_memo(target, numbers, memo={}):
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
        memo[target] = has_sum_memo(remainder, numbers, memo)

        if memo[target] is not None:
            memo[target].append(number)
            return(memo[target])

    memo[target] = None

    return(None)


if __name__ == "__main__":
    """
    exercising functions from the command line
    """

    print("running has_sum_memo:")
    print("has_sum_memo(300, [7, 14]) -> {}"
          .format(has_sum_memo(300, [7, 14])))

    print("has_sum_memo(100, [10, 25]) -> {}"
          .format(has_sum_memo(100, [10, 25])))

    print()
    print("----------------------------------------------------------")
    print()

    print("running has_sum_rec:")
    print("has_sum_rec(300, [7, 14]) -> {}"
          .format(has_sum_rec(300, [7, 14])))
