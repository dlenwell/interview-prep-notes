"""
base classes used in examples in this folder.

bare bones Node and LinkedList objects with no frills.

"""
from random import randint


class Node():
    """
    base Node object
    """
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class LinkedList():
    """
    base LinkedList object
    """

    def __init__(self, list = []):
        """
        """
        self.sorted = False
        self.length = 0
        self.head = None

        if len(list) > 0:
            self.import_unordered(list)
            self.sorted = True


    def increase_length(self):
        """
        """
        self.length = self.length + 1


    def import_unordered(self, list):
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


    def import_ordered(self, list):
        """
        imports a linked list from a python list object
        """
        self.head = Node(list[0])

        for item in list[1:]:
            self.insert(item)


    def string(self):
        """
        iterative function that prints the linked list like this..

        item -> item2 ->


        """
        node = self.head
        output = ""

        while node:
            end = "-> "
            if not node.next:
                 end = "-> None"
            output = "{}{}{}".format(output, node.data, end)

            node = node.next

        return(output)


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


    def insert(self, new):
        """
        Function to insert a new node in the sorted order.

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


    def delete(self, value):
        """
        deletes nodes with the provided value
        """
        node = self.head
        last = None

        while node:
            if node.data == value:
                if last is not None:
                    next = node.next
                    last.next = next
                    node.next = None
                    node = next
                else:
                    next = node.next
                    node.next = None
                    node = next
            else:
                last = node
                node = node.next


def generate_list(length = 50):
    """
    generates a list to play with
    """
    list = []
    for i in range(1,length + 1):
        list.append(randint(1,9999))

    return(list)


if __name__ == "__main__":
    """
    only run this code to exercise it via the command line.

    """
    print()
    print('creating new linked list with these values [1,2,3,4,5,6,6,6,7,8,9]')
    LinkedList = LinkedList([1,2,3,4,5,6,6,6,7,8,9])

    print("__________________________________________")
    print()
    print("before list: {}".format(LinkedList.string()))

    print()
    LinkedList.delete(6)
    print("deleting 6")
    print()

    print("after delete: {}".format(LinkedList.string()))
    print()
    print("__________________________________________")
    print()
