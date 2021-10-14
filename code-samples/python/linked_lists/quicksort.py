"""
Quick sort

this is a classic recursive quicksort method that uses recursion

basically it uses the last number in the sequence as a "pivot" and sorts
items that are less than the pivot in one group and more in another.

then concats sub calls of the two sides together. in the end you end up
with a sorted list.
"""
from base import LinkedList, Node, generate_list
from collections import deque

class LinkedListQuickSort(LinkedList):
    """
    LinkedListSort object extends the base LinkedList class
    """

    def quick_sort(self, sequence):
        """
        recursive quicksort method
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

        return(self.quick_sort(lesser) + [pivot] + self.quick_sort(greater))


    def sort(self):
        """
        this method converts the linked list into a python list object to pass
        into the quicksort recursive method and then rewrites the data on
        the linked list in the now sorted order.

        """
        sequence = []
        node = self.head

        while node:
            sequence.append(node.data)
            node = node.next

        sequence = deque(self.quick_sort(sequence))

        node = self.head

        while node:
            node.data = sequence.popleft()
            node = node.next

        self.sorted = True


if __name__ == "__main__":
    """
    main function for calling this script to exercise it via the command line.

    """
    print()
    print('Generating a new unsorted list with 12 random numbers...')
    LinkedList = LinkedListSort(generate_list(12))

    print("__________________________________________")
    print()
    print("unsorted list: {}".format(LinkedList.string()))

    print()
    print("running quick sort...")
    print()
    LinkedList.sort()
    print("sorted list: {}".format(LinkedList.string()))
    print()
    print("__________________________________________")
    print()
