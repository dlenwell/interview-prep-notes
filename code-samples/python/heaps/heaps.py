"""
MinHeap object

in a min heap all children are larger than their parents

heap =
  - parent node only has two children
  - must be complete tree except last level


example heap:

                  ┌--89
            ┌--31 ┤
            │     └--39
      ┌--04 ┤
      │     │     ┌--49
      │     └--15 ┤
      │           │     ┌--58
      │           └--47 ┤
      │                 └--56
 --04 ┤
      │                 ┌--79
      │           ┌--45 ┤
      │           │     └--65
      │     ┌--41 ┤
      │     │     │     ┌--48
      │     │     └--42 ┤
      │     │           └--54
      └--19 ┤
            │           ┌--77
            │     ┌--30 ┤
            │     │     └--39
            └--28 ┤
                  │     ┌--90
                  └--29 ┤
                        └--69
"""
import math
from pptree import *

"""

"""
class MinHeap:

    def __init__(self, capacity):
        """
        """
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0


    def getParentIndex(self, index):
        """
        """
        return (index - 1) // 2


    def getLeftChildIndex(self, index):
        """
        """
        return( 2 * index + 1 )


    def getRightChildIndex(self, index):
        """
        """
        return( 2 * index + 2 )


    def hasParent(self, index):
        """
        """
        return self.getParentIndex(index) >= 0


    def hasLeftChild(self, index):
        """
        """
        return self.getLeftChildIndex(index) < self.size


    def hasRightChild(self, index):
        """
        """
        return self.getRightChildIndex(index) < self.size


    def parent(self, index):
        """
        """
        return self.storage[self.getParentIndex(index)]


    def leftChild(self, index):
        """
        """
        return self.storage[self.getLeftChildIndex(index)]


    def rightChild(self, index):
        """
        """
        return self.storage[self.getRightChildIndex(index)]


    def isFull(self):
        """
        """
        return self.size == self.capacity


    def swap(self, index1, index2):
        """
        """
        temp = self.storage[index1]

        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp


    ## iterative versions of the insert and sort methods
    def heapifyUp(self):
        """
        """
        index = self.size - 1
        while (self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)


    def heapifyDown(self):
        """
        """
        index = 0

        while(self.hasLeftChild(index)):
            smallerChildIndex = self.getLeftChildIndex(index)
            if (self.hasRightChild(index) and self.rightChild(index) < self.leftChild(index)):
                smallerChildIndex = self.rightChild(index)

            try:
                if (self.storage[index] < self.storage[smallerChildIndex]):
                    break
                else:
                    self.swap(index, smallerChildIndex)

                index = smallerChildIndex
            except IndexError:
                break


    def insert(self, data):
        """
        """
        if (self.isFull()):
            raise("Heap is full")

        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp()


    def removeMin(self):
        """
        """
        if (self.size == 0):
            raise("Empty Heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown()

        return(data)


    ## recursive versions of the insert and sort functions
    def heapifyDownRecursive(self, index):
        """
        """
        smallest = index

        if (self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.hasLeftChild(index)

        if (self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)

        if (smallest != index):
            self.swap(index, smallest)
            self.heapifyDownRecursive(smallest)



    def heapifyUpRecursive(self, index):
        """
        """
        if (self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUpRecursive(self.getParentIndex(index))


    def insertRecursive(self, data):
        """
        """
        if (self.isFull()):
            raise("Heap is full")

        self.storage[self.size] = data
        self.size += 1
        self.heapifyUpRecursive(self.size - 1)


    def removeMinRecursive(self):
        """
        """
        if (self.size == 0):
            raise("Empty Heap")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDownRecursive(0)

        return(data)


    def printHeap(self):
        """

        """
        nodes = {}

        nodes['0'] = Node("--{} ".format(str(self.storage[0]).zfill(2)),)

        for index in range(len(self.storage)):

            if self.hasParent(index):
                nodes[str(index)] = Node(
                    "--{} ".format(str(self.storage[index]).zfill(2)),
                    nodes[str(self.getParentIndex(index))]
                )

        print_tree(nodes['0'], horizontal=True)


def main():
    """ Just a test program so you can see things working.
    """
    print("program running")


    print("populating heap with random numbers")
    heap = MinHeap(25)
    for i in range(25):
        heap.insert(random.randrange(0,99))

    heap.printHeap()

    sleep(1)
    print("removing min")
    heap.removeMin()
    heap.printHeap()

    sleep(1)
    print("inserting another value")
    heap.insert(random.randrange(0,99))
    heap.printHeap()
    #    sleep(1)


if __name__ == "__main__":
    from time import sleep
    import random

    main()
