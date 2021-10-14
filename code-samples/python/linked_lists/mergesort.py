"""
Merge Sort o(n*log^n)


uses 4 funcitons:

sort  <- initial call kicks off the sort with the objects head
merge_sort <- recursive function that splits > sorts > merges
middle <- helper function to find the middle of the list
merge <- helper function to merge two lists in order


"""
import time
from base import LinkedList, Node, generate_list


class LinkedListMergeSort(LinkedList):
    """
    LinkedListSort object extends the base LinkedList class
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


    def merge_sort(self, head: Node) -> Node:
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

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        return(self.merge(left, right))


    def sort(self):
        """
        starter call for merge sort to make it use the self.head variable to
        start a sort.
        """
        self.head = self.merge_sort(self.head)


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
    print("running merge sort...")
    print()
    LinkedList.sort()
    print("sorted list: {}".format(LinkedList.string()))
    print()
    print("__________________________________________")
    print()
