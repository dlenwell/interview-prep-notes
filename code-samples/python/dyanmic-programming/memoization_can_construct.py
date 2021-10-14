"""
can construct

Write a function `can_construct(target, words)` that takes in a target
string and an array of strings.

The function should return a boolean indicating whether or not the target
can be strongucted by concatenating the elements of the word bank array.

You may resuse elements of `words` as many times as needed.

Example:

> can_construct(target, [])

Complexity:

recursive time: 0(n^m * m)
recursive space: 0(m^2)

memoized time: 0(n*m^2)
space: 0(m^2)

"""
import time


def can_construct_rec(target, words):
    """
    recursive version of the call
    """
    if target == "":
        return(True)

    for word in words:
        if target.startswith(word):
            suffix = target.lstrip(word)

            if can_construct_rec(suffix, words) is True:
                return(True)

    return(False)


def can_construct_memo(target, words, memo={}):
    """
    memoized version of the function
    """
    if target in memo.keys():
        return(memo[target])
    if target == "":
        return(True)

    for word in words:
        if target.startswith(word):
            suffix = target.lstrip(word)

            if can_construct_rec(suffix, words) is True:
                memo[target] = True
                return(True)

    memo[target] = False
    return(False)


def race(target, words):
    """
    race
    """
    print("running can_construct_memo with target:{} words:{}"
          .format(target, words))

    # with memoization
    start = time.time()
    print(
        "can_construct_memo({}, {}) -> {}".format(
            target,
            words,
            can_construct_memo(target, words)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))

    print()
    print()

    # recursion
    print("running can_construct_rec with target:{} words:{}"
          .format(target, words))

    start = time.time()
    print(
        "can_construct_rec({}, {}) -> {}".format(
            target,
            words,
            can_construct_rec(target, words)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


if __name__ == "__main__":
    """
    race the functions
    """
    race("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd'])
    race("skateboard", ['bo', 'rd', 'ate', 't', 'ska', "sk", "boar"])
    race("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    race("running can_construct_rec with target.",
         ["run", "n", "in`", "g", "Con", " ", "tar",
          "ge", "t", ".", "c", "a", "structRec", "with"])
