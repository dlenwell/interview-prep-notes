"""


Tree inversion





"""
from tree import Node, Tree


class InvertTree(Tree):
    """
    InvertTree Tree class extends the base Tree class and just adds the invert
    functions.

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


    def invert(self):
        """
        invert tree
        """
        self.invert_aux(self.root)



def main():
    """
    main exercise run through...
    """
    import random

    tree = InvertTree()
    unsorted_node_values = []

    print('generating tree with 100 nodes with random values between 1 and 999')

    # add 100 random values to the tree
    for i in range(10):
        value = random.randint(1,999)
        unsorted_node_values.append(value)
        tree.add(value)

    print()
    tree.print()
    print()
    print('Inverting tree:')

    tree.invert()
    print()
    tree.print()
    print()
    print()

if __name__ == "__main__":
    main()
