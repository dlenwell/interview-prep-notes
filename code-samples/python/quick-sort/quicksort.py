#!/usr/bin/env python3
"""
quick sort
"""


def split(sequence, start_index, pivot_index):
    """
    Set pivot element at its correct position in sorted array
    """
    index = (start_index - 1)

    for sort_index in range(start_index, pivot_index):
        if sequence[sort_index] <= sequence[pivot_index]:
            # increment index of smaller element
            index += 1
            sequence[index], sequence[sort_index] = \
                sequence[sort_index], sequence[index]

    sequence[index + 1], sequence[pivot_index] = \
        sequence[pivot_index], sequence[index + 1]

    return(index + 1)


def quick_sort_iterative(sequence):
    """
    iterative version
    """
    start_index = 0
    pivot = len(sequence) - 1
    # Create an auxiliary stack
    size = pivot - start_index + 1
    stack = [0] * (size)

    # initialize top of stack
    top = -1

    # push initial values of start_index and pivot to stack
    top = top + 1
    stack[top] = start_index
    top = top + 1
    stack[top] = pivot

    # Keep popping from stack while is not empty
    while top >= 0:
        # Pop pivot and l
        pivot = stack[top]
        top = top - 1
        start_index = stack[top]
        top = top - 1

        partition = split(sequence, start_index, pivot)

        # If there are elements on left side of pivot,
        # then push left side to stack
        if partition - 1 > start_index:
            top = top + 1
            stack[top] = start_index
            top = top + 1
            stack[top] = partition - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if partition + 1 < pivot:
            top = top + 1
            stack[top] = partition + 1
            top = top + 1
            stack[top] = pivot

    return(sequence)


def quick_sort_recursive(sequence):
    """
    quick sort recursive method
    """
    if len(sequence) <= 1:
        return(sequence)
    else:
        pivot = sequence.pop()

    lesser = []
    greater = []

    for item in sequence:
        if item > pivot:
            greater.append(item)
        else:
            lesser.append(item)

    return(quick_sort_recursive(lesser) +
           [pivot] +
           quick_sort_recursive(greater))
