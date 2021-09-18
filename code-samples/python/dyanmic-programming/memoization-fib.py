"""
Memoization excersize

There are two functions in this file that will provide the value for any position
in the fibinacci sequence. One is strictly recursive while the other is recursive
but takes advantage of memoization techniques to speed things up dramatically.

to test call this file from a command line with any integer as the argument.

>  python3 memoization.py 25

What you will find out is that with smaller numbers in the sequence recursion on
its own is much faster than using memoization mostly because of the overhead
involved in building the memo and checking against it on every iteration.

This shifts back into memoizations favor once you try to calculate more than
35 digits.

my tests of testing n=50 resulted in around 7.8 seconds for the memoization
version and over an hour to do recursively on a pretty fast computer.

"""
import time
import sys

def fib_recursive(n):
    """
        This is a purely recursive version of the function.

        Because its not caching the calculations its doing on each branch of the
        sequence it is doomed to repeat itself and has to painstakingly traverse
        the entire tree of values which if you are trying to find the 50th
        integer in the sequence will take over a quadrillian iterations.
    """
    if n <= 2:
        return 1

    return( int(fib_recursive(n - 1)) + int(fib_recursive(n - 2)))



def fib(n, memo = {}):
    """
        This is the memoized version of the function.

        It takes advantage of a hash table that is shared with each recursion
        that holds cached results from any depth first traversal of the tree and
        as such saves itself from falling into the traps of exponential number
        traps.
    """
    if n in memo.keys():
        return memo[n]

    if n <= 2:
        return 1

    memo[n] = int(fib(n - 1, memo)) + int(fib(n - 2, memo))

    return(memo[n])


def race(n):
    """
        This runs the memoization version of the fib function against the
        recursive version and outputs the time it takes to calculate each one

        Sample output:
        running fib with argument 40 with memoization...
        fib(40) -> 102334155
        run time: 4.38690185546875e-05


        running fib with argument 40 recursively...
        fib_recursive(40) -> 102334155
        run time: 50.607287883758545

    """
    print("running fib with argument {} with memoization...".format(n))

    start_ = time.time()
    print("fib({}) -> {}".format(n,fib(n)))
    end_ = time.time()
    print("run time: {}".format(end_ - start_))

    print()
    print()

    print("running fib with argument {} recursively...".format(n))

    start = time.time()
    print("fib_recursive({}) -> {}".format(n,fib_recursive(n)))
    end = time.time()

    print("run time: {}".format(end - start))
    print()
    print()


def main():
    """
        main program
    """
    default_fib_depth = 10

    if not sys.argv:
        depth = default_fib_depth
    else:
        depth = int(sys.argv[1])

    race(depth)


if __name__ == "__main__":
    main()
