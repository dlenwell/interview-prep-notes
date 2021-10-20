"""
sliding window examples

- max_sum -> (maximum sequential sum in sequence no greater than length input)
- shortest_larger_than -> (shortest sub array with sum larger than input)

"""


def max_sum(sequence, length):
    """
    finds the largest continuous sum in the sequence of length
    """
    largest = float('-inf')
    start = 0
    sum = 0

    for pointer, value in enumerate(sequence):
        sum += value

        if pointer - start + 1 == length:
            largest = max(largest, sum)
            sum -= sequence[start]
            start += 1

    return(largest)


def shortest_larger_than(sequence, max):
    """
    finds the lenth of the shorted subarray that is larger than in max value
    """
    shortest = float('inf')
    start = 0
    sum = 0

    for pointer, value in enumerate(sequence):
        sum += value

        while sum >= max:
            shortest = min(shortest, pointer - start + 1)
            sum -= sequence[start]
            start += 1

    return(shortest)


def main():

    print("max_sum([4,3,1,2,3,5,3,2,8], 3) -> ",
          max_sum([4, 3, 1, 2, 3, 5, 3, 2, 8], 3))
    print()

    print("shortest_larger_than([4,3,1,2,3,5,3,2,8], 12) -> ",
          shortest_larger_than([4, 3, 1, 2, 3, 5, 3, 2, 8], 12))


if __name__ == "__main__":
    """
    """
    main()
