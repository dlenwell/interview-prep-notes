"""
    best Sum

    Write a function `canConstruct(target, words)` that takes in a target string
    and an array of strings.

    The function should return a boolean indicating whether or not the target
    can be strongucted by concatenating the elements of the word bank array.

    You may resuse elements of `words` as many times as needed.


    Example:

    > canConstruct(target, [])

    Complexity:

    recursive time: 0(n^m * m)
    recursive space: 0(m^2)

    memoized time: 0(n*m^2)
    space: 0(m^2)


"""
import time
import sys


def canConstructRec(target, words):
    """
        recursive version of the call
    """
    if target == "":
        return(True)

    for word in words:
        if target.startswith(word):
            suffix = target.lstrip(word)

            if canConstructRec(suffix, words) is True:
                return(True)

    return(False)


def canConstructMemo(target, words, memo = {}):
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

            if canConstructRec(suffix, words) is True:
                memo[target] = True
                return(True)

    memo[target] = False
    return(False)


def race(target, words):
    """
        race
    """
    print("running canConstructMemo with target:{} words:{} using memoization..."
          .format(target, words))

    # with memoization
    start = time.time()
    print(
        "canConstructMemo({}, {}) -> {}".format(
            target,
            words,
            canConstructMemo(target, words)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))


    print()
    print()

    # recursion
    print("running canConstructRec with target:{} words:{} using recursion..."
          .format(target, words))

    start = time.time()
    print(
        "canConstructRec({}, {}) -> {}".format(
            target,
            words,
            canConstructRec(target, words)
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


    race( "abcdef", ['ab','abc','cd','def', 'abcd'])
    race( "skateboard", ['bo','rd','ate','t', 'ska', "sk", "boar"])
    race( "enterapotentpot",["a","p", "ent", "enter", "ot", "o", "t"])
    race( "running canConstructRec with target.",
         ["run", "n", "in`", "g", "Con", " ", "tar",
          "ge", "t", ".", "c","a", "structRec", "with"])


if __name__ == "__main__":
    main()
