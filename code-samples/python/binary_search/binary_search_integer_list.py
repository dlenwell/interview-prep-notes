"""
Binary search index of in sorted list

Mission:

Implement both an iterative and recursive version of an indexOf function that
returns the index of a given value in a sorted list.

"""
import time


# CONSTANTS
HAYSTACK = [0, 5, 8, 12, 20, 31, 33, 40, 50, 56, 73, 79, 83, 85, 90, 94, 101,
            108, 115, 118, 153, 159, 160, 161, 172, 175, 198, 198, 198, 200,
            207, 209, 213, 216, 228, 232, 235, 247, 252, 252, 258, 262, 262,
            267, 267, 270, 274, 274, 282, 287, 292, 303, 310, 314, 318, 329,
            332, 337, 342, 345, 345, 350, 354, 359, 361, 365, 365, 369, 387,
            389, 395, 400, 407, 410, 412, 414, 414, 415, 415, 417, 423, 430,
            431, 433, 434, 445, 449, 450, 453, 455, 457, 460, 466, 467, 472,
            478, 478, 488, 493, 497]

NEEDLE = 292


def index_of_iterative(haystack, needle):
    """
    """
    left = 0
    right = len(haystack)

    while left <= right:

        center = (left + right) // 2

        if haystack[center] == needle:
            return (center)

        elif needle < haystack[center]:
            right = center - 1

        else:
            left = center + 1

    return(None)


def index_of_recursive(haystack, needle, left=0, right=None):
    """
    """
    if not right:
        right = len(haystack)
    if left > right:
        return(None)

    center = (left + right) // 2

    if haystack[center] == needle:
        return(center)

    elif needle < haystack[center]:
        return(index_of_recursive(haystack, needle, left, (center - 1)))

    else:
        return(index_of_recursive(haystack, needle, (center + 1), right))

    return(None)


def race(haystack, needle):
    """
        race
    """
    print("running index_of_recursive with haystack:{} needle:{}   ::"
          .format(haystack, needle))

    # with memoization
    start = time.time()
    print(
        "index_of_recursive({}, {}) -> {}".format(
            haystack, needle,
            index_of_recursive(haystack, needle)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))

    print()
    print()

    # recursion
    print("running index_of_iterative with haystack:{} needle:{} ::"
          .format(haystack, needle))

    start = time.time()
    print(
        "index_of_iterative({}, {}) -> {}".format(
            haystack,
            needle,
            index_of_iterative(haystack, needle)
        )
    )
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()


if __name__ == "__main__":
    """
    do the things
    """
    race(HAYSTACK, NEEDLE)
