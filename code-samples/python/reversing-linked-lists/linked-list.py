"""


"""
import time
from random import randint
import collections

class Node():
    """
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    """
    LinkedList object.
    """

    def __init__(self, list = []):
        """
        """
        self.sorted = False
        self.length = 0
        self.head = None

        if len(list) is not 0:
            self.import_from_list(list)


    def increase_length(self):
        """
        """
        self.length = self.length + 1


    def import_from_list(self, list):
        """
        imports a linked list from a python list object
        """
        if self.head is None:
            self.head = Node(list[0])
            starting_index = 1
        else:
            starting_index = 0

        for item in list[starting_index:]:
            node = self.head

            while node.next:
                node = node.next

            node.next = Node(item)

        self.length = self.length + len(list)
        self.sorted = False


    def import_from_list_in_order(self, list):
        """
        imports a linked list from a python list object
        """
        self.head = Node(list[0])

        for item in list[1:]:
            self.insert(item)


    def print(self):
        """
        iterative function that prints the linked list like this..

        item -> item2 ->


        """
        node = self.head

        print('', end = "")

        while node:
            end = ""
            if node.next:
                 end = "-> "
            print(node.data, end = end)

            node = node.next

        print('')


    def recursive_reverse_aux(self, current, previous):
        """
        actually the recursive reverse function

        """
        if current.next is None:
            self.head = current
            self.head.next = previous
            return()

        # Save current.next node for recursive call
        next = current.next

        # And update next
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


    """
    Quick sort
    """
    def quick_sort_aux(self, sequence):
        """
        this is a classic quicksort method that uses recursion

        basically it uses the last number in the sequence as a "pivot" and sorts
        items that are less than the pivot in one group and more in another.

        then concats sub calls of the two sides together. in the end you end up
        with a sorted list.

        

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

        return(self.quick_sort_aux(lesser) +
               [pivot] +
               self.quick_sort_aux(greater))


    def quick_sort(self):
        """

        """
        sequence = []
        node = self.head

        # convert linked list to a python list
        while node:
            sequence.append(node.data)
            node = node.next

        #
        sequence = collections.deque(self.quick_sort_aux(sequence))

        node = self.head

        while node:
            node.data = sequence.popleft()
            node = node.next

        self.sorted = True


    """
    Merge Sort o(n * log n)

    uses 4 funcitons:

    merge_sort  <- initial call kicks off the sort with the objects head
    merge_sort_aux <- recursive function that splits > sorts > merges
    middle <- helper function to find the middle of the list
    merge <- helper function to merge two lists in order
    """
    def middle(self, head):
        """
        find the middle
        """
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return(slow)


    def merge(self, left, right):
        """
        merge two lists and keep order
        """
        tail = dummy = Node()

        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next

            tail = tail.next

            if left is not None:
                tail.next = left
            elif right is not None:
                tail.next = right

        return dummy.next


    def merge_sort_aux(self, head: Node) -> Node:
        """
        merge sort method with strict typing

        """
        if not head or not head.next:
            return(head)

        # split it
        left = head
        right = self.middle(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.merge_sort_aux(left)
        right = self.merge_sort_aux(right)

        return(self.merge(left, right))


    def merge_sort(self):
        """
        starter call for merge sort to make it use the self.head variable to
        start a sort.
        """
        self.head = self.merge_sort_aux(self.head)


    def bubble_sort(self):
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


    def sort(self):
        """this is an ugly way of sorting the list.

        it essentially dumps the list into a python list object uses the built
        in method to sort the array in numerical order which is log ^n all by
        it self and then iterates it again to resets the pointers and the data
        it as a linked list.


        """
        values = []
        node = self.head

        while node:
            values.append(node.data)
            node = node.next

        values.sort()
        values = collections.deque(values)

        node = self.head

        while node:
            node.data = values.popleft()
            node = node.next

        self.sorted = True


    def insert(self, new):
        """
        Function to insert a new node at the beginning

        """
        if self.head is None:
            self.head = Node(new)
            self.sorted = True
            self.increase_length()
            return()

        if not self.sorted:
            self.sort()

        last = None
        current = self.head

        while(current is not None):
            # if the new data is the lowest in the stack and needs to be the
            # new head.
            if last is None and new < current.data:
                new_node = Node(new)
                new_node.next = self.head
                self.head = new_node

                break

            # if we landed between two datas where the new data sits.
            elif current.next is not None and \
                new > current.data and new <= current.next.data:
                last = current
                next = current.next
                current = Node(new)
                current.next = next
                last.next = current

                break

            # if we have reached the end of the chain and are bigger than
            # everything else.
            elif new > current.data and current.next is None:
                last = current
                current = Node(new)
                last.next = current

                break

            next = current.next
            last = current
            current = next

        self.increase_length()


    def push(self, new_data):
        """
        Function to insert a new node at the beginning
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

        # now that we've just jammed something in front of it
        # we have to tell the object its no longer sorted.
        self.sorted = False
        self.increase_length()


def generate_list(length = 50):
    """
    generates a list to play with
    """
    list = []
    for i in range(1,length + 1):
        list.append(randint(1,9999))

    return(list)


def main():
    """
    main function for calling this script to exercise it via the command line.

    """
    print()
    print('Generating a new unsorted list with 900 random numbers...')
    list = generate_list(100)
    LinkedList1 = LinkedList(list)
    LinkedList2 = LinkedList(list)
    LinkedList3 = LinkedList(list)
    LinkedList4 = LinkedList(list)
    print()
    print("__________________________________________")
    print()
    print("racing sort methods...")
    print()
    print("sorting via timslist:")
    start = time.time()
    LinkedList1.sort()
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()
    # bubble sort
    print("sorting via bubble sort:")
    start = time.time()
    LinkedList2.bubble_sort()
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    # bubble sort
    print("sorting via merge sort:")
    start = time.time()
    #LinkedList3.print()
    LinkedList3.merge_sort()
    #LinkedList3.print()
    end = time.time()
    print("run time: {}".format(end - start))
    print()

    print("sorting via quick sort:")
    start = time.time()
    LinkedList4.print()
    LinkedList4.quick_sort()
    LinkedList4.print()
    end = time.time()
    print("run time: {}".format(end - start))
    print()

    print("__________________________________________")
    print()
    print("Racing reverse methods...")
    print()
    print("reverse with recursion:")
    start = time.time()
    LinkedList1.iterative_reverse()
    end = time.time()
    print("run time: {}".format(end - start))
    print()
    print()
    print("reverse with iteration:")

    try:
        start = time.time()
        LinkedList2.recursive_reverse()
        end = time.time()
        #bubblesort.print()
        print("run time: {}".format(end - start))
    except RecursionError:
        print("Violates recursion depth limits on this machine.")

    print()


if __name__ == "__main__":
    main()
