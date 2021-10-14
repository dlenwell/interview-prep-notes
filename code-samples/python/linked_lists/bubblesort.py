"""
Bubble sort

"""
import time
from base import LinkedList, Node, generate_list
from collections import deque

class LinkedListBubble(LinkedList):
    """
    LinkedListSortable object extends the base LinkedList class
    """

    def sort(self):
        """
        classic iterative bubble sort method.

        """
        end = None

        while end != self.head:
            current = self.head

            while current.next != end:
                next = current.next

                if current.data > next.data:
                    current.data, next.data = next.data, current.data

                current = current.next

            end = current


if __name__ == "__main__":
    """
    only run this code to exercise it via the command line.

    """
    print()
    print('Generating a new unsorted list with 12 random numbers...')
    LinkedList = LinkedListBubble(generate_list(12))

    print("__________________________________________")
    print()
    print("unsorted list: {}".format(LinkedList.string()))

    print()
    print("running Bubble sort...")
    print()
    LinkedList.sort()
    print("sorted list: {}".format(LinkedList.string()))
    print()
    print("__________________________________________")
    print()
