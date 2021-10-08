import time
from base import generate_list
from reverse import LinkedListReverse
from bubblesort import LinkedListBubble
from mergesort import LinkedListMergeSort
from quicksort import LinkedListQuickSort

if __name__ == "__main__":
    """
    only run this code to exercise it via the command line.

    """
    print()
    print('Generating a new unsorted list with 900 random numbers...')
    list = generate_list(500)

    print()
    print("__________________________________________")

    print()
    print("racing sort methods...")
    print()

    # bubble sort
    print("sorting via bubble sort:")
    LinkedList_Bubble = LinkedListBubble(list)
    start = time.time()
    LinkedList_Bubble.sort()
    end = time.time()
    print("run time: {}".format(end - start))
    print()

    # merge sort
    print("sorting via merge sort:")
    LinkedList_Merge = LinkedListMergeSort(list)
    start = time.time()
    LinkedList_Merge.sort()
    end = time.time()
    print("run time: {}".format(end - start))
    print()

    # quicksort
    print("sorting via quick sort:")
    LinkedList_QuickSort = LinkedListQuickSort(list)
    start = time.time()
    LinkedList_QuickSort.sort()
    end = time.time()
    print("run time: {}".format(end - start))
    print()

    print("__________________________________________")

    print()
    reverse_list = LinkedListReverse(list)
    print("Racing reverse methods...")
    print()
    print("reverse with recursion:")
    start = time.time()
    reverse_list.iterative_reverse()
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()
    print("reverse with iteration:")

    try:
        start = time.time()
        reverse_list.recursive_reverse()
        end = time.time()
        print("run time: {}".format(end - start))

    except RecursionError:
        print("Violates recursion depth limits on this machine.")

    print()
