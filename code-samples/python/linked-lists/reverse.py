"""


"""
import time
from base import LinkedList, Node, generate_list

class LinkedListReverse(LinkedList):
    """
    LinkedListReverse object extends the base LinkedList class
    """

    def recursive_reverse_aux(self, current, previous):
        """
        recursive reverse function

        """
        if current.next is None:
            self.head = current
            self.head.next = previous
            return()

        next = current.next
        current.next = previous

        self.recursive_reverse_aux(next, current)


    def recursive_reverse(self):
        """
        helper function to trigger the recursive reverse without passing in
        the head. Since this is an object the starting head should always be
        self.head
        """
        if self.head is None:
            return()
        self.recursive_reverse_aux(self.head, None)


    def iterative_reverse(self):
        """
        iterative function to reverse the linked list.
        """
        last = None
        current = self.head

        while(current is not None):
            next = current.next
            current.next = last
            last = current
            current = next

        self.head = last


if __name__ == "__main__":
    """
    main function for calling this script to exercise it via the command line.

    """
    print()
    print('Generating a new unsorted list with 900 random numbers...')
    list = generate_list(250)
    LinkedList = LinkedListReverse(list)

    print("__________________________________________")
    print()
    print("Racing reverse methods...")
    print()
    print("iterative reverse:")
    start = time.time()
    LinkedList.iterative_reverse()
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()
    print("recursive reverse:")

    try:
        start = time.time()
        LinkedList.recursive_reverse()
        end = time.time()
        print("run time: {}".format(end - start))
    except RecursionError:
        print("Violates recursion depth limits.")

    print()
