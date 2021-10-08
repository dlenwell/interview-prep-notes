"""
Quick sort
"""


def quick_sort(sequence):
    """
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

    return(quick_sort(lesser) + [pivot] + quick_sort(greater))



if __name__ == "__main__":
    sequence = [1,4,45,90,300,12,24,19]

    quick_sort(sequence)
