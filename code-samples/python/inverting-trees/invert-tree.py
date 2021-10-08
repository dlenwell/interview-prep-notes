"""
Tree inversion:

Inverting a binary tree is a common programming task in tech screening
interviews.

Example output:
generating tree with 100 nodes with random values between 1 and 999

     ____346______________________
    /                             \
  _181_          ________________973
 /     \        /
138   335     _576_
             /     \
            502   599__________
                               \
                          ____843
                         /
                       _764_
                      /     \
                     759   818

Inverting tree with recursion:

  ______________________346____
 /                             \
973________________          _181_
                   \        /     \
                 _576_     335   138
                /     \
     __________599   502
    /
   843____
          \
        _764_
       /     \
      818   759

Inverting tree with iterative style:

     ____346______________________
    /                             \
  _181_          ________________973
 /     \        /
138   335     _576_
             /     \
            502   599__________
                               \
                          ____843
                         /
                       _764_
                      /     \
                     759   818

"""
from tree import Node, Tree
from collections import deque

class InvertTree(Tree):
    """
    InvertTree Tree class extends the base Tree class and just adds the invert
    functions.

    This class includes a recursive and an iterative version of the function.

    """

    def invert_aux(self, node):
        """
        invert tree
        """
        # entry point
        if node is None:
            return(None)

        # invert my children
        node.left, node.right = \
            self.invert_aux(node.right), self.invert_aux(node.left)

        return(node)


    def recursive_invert(self):
        """
        invert tree
        """
        self.invert_aux(self.root)


    def invert_iterative(self):
        """
        iterative function to invert the binary tree using a queue
        """
        queue = deque()
        queue.append(self.root)

        while queue:
            current = queue.popleft()
            current.left, current.right = current.right, current.left

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)


def main():
    """
    main exercise run through...
    """
    import random

    tree = InvertTree()
    unsorted_node_values = []

    print('generating tree with 100 nodes with random values between 1 and 999')

    # add 100 random values to the tree
    for i in range(12):
        value = random.randint(1,999)
        unsorted_node_values.append(value)
        tree.add(value)

    print()
    tree.print()
    print()
    print('Inverting tree with recursion:')

    tree.recursive_invert()
    print()
    tree.print()
    print()
    print('Inverting tree with iterative style:')
    tree.invert_iterative()
    print()
    tree.print()

    print()
    print()

if __name__ == "__main__":
    main()
