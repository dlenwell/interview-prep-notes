"""
generic tree base to build off of.
"""
from ansimarkup import ansiprint as print


class Node():
    """
    Node object
    """

    def __init__(self, value, parent = None):
        """
        """
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    ## helper functions
    def has_left_child(self):
        """
        """
        if self.left is not None:
            return(True)
        return(False)


    def has_right_child(self):
        """
        """
        if self.right is not None:
            return(True)
        return(False)


    def has_parent(self, node):
        """
        """
        if self.parent is not None:
            return(True)
        return(False)


    def _print_aux(self, highlight = None):
        """
        helper function for print feature in tree object.

        uses recursion to build lines for displaying a tree

        supports passing in a string to highlight in green text in the output

        Returns list of strings, width, height, and horizontal coordinate of
        the root.

        Because it has to display the entire tree this method requires
        that you fully traverse the tree. This is not the most efficient way
        to search the tree.. but nescesarry if you want to see the entire tree
        with the search result highlighted it.
        """

        if highlight is not None and str(self.value) == str(highlight):
            value = "<b><green>{}</green></b>".format(self.value)
        else:
            value = '{}'.format(self.value)

        value_len = len(str(self.value))

        # No child
        if self.right is None and self.left is None:
            line = value
            width = value_len
            height = 1
            middle = width // 2

            return([line], width, height, middle)

        # Only left
        if self.right is None:
            lines, width, height, middle = self.left._print_aux(highlight)

            first_line = \
                (middle + 1) * ' ' + (width - middle - 1) * '_' + value
            second_line = \
                middle * ' ' + '/' + (width - middle - 1 + value_len) * ' '
            shifted_lines = [line + value_len * ' ' for line in lines]

            return(
                [first_line, second_line] + shifted_lines, # next set of lines
                width + value_len,
                height + 2,
                width + value_len // 2
            )

        # Only right
        if self.left is None:
            lines, width, height, middle = self.right._print_aux(highlight)

            first_line = value + middle * '_' + (width - middle) * ' '
            second_line = \
                (value_len + middle) * ' ' + '\\' + (width - middle - 1) * ' '
            shifted_lines = [value_len * ' ' + line for line in lines]

            return(
                [first_line, second_line] + shifted_lines,
                width + value_len,
                height + 2,
                value_len // 2
            )

        # both
        left, l_width, l_height, l_middle = self.left._print_aux(highlight)
        right, r_width, r_height, r_middle = self.right._print_aux(highlight)

        first_line = (l_middle + 1) * ' ' + (l_width - l_middle - 1) * '_' + \
            value + r_middle * '_' + (r_width - r_middle) * ' '
        second_line = l_middle * ' ' + '/' + (l_width - l_middle - 1 + \
            value_len + r_middle) * ' ' + '\\' + (r_width - r_middle - 1) * ' '

        if l_height < r_height:
            left += [l_width * ' '] * (r_height - l_height)
        elif r_height < l_height:
            right += [r_width * ' '] * (l_height - r_height)

        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + value_len * ' ' + b for a, b in zipped_lines]

        return(
            lines,
            l_width + r_width + value_len,
            max(l_height, r_height) + 2,
            l_width + value_len // 2
        )


class Tree():
    """
    Tree class

    root object for the node object above.
    """

    def __init__(self, node = None):
        """
        init method

        optionally pass in a node to become the root node.
        """
        self.root = node

        if self.root is None:
            self.node_count = 0
        else:
            self.node_count = 1


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


    def add_node_count(self):
        self.node_count = self.node_count + 1


    def add(self, value, current = None):
        """
        add

        recursive add function
        """
        if self.root is None:
            self.root = Node(value)
            self.add_node_count()
        else:
            if current is None:
                current = self.root

            if value < current.value:
                if current.left is None:
                    current.left = Node(value, current)
                    self.add_node_count()
                else:
                    self.add(value, current.left)
            else:
                if current.right is None:
                    current.right = Node(value, current)
                    self.add_node_count()
                else:
                    self.add(value, current.right)


    def print(self, highlight = None):
        """
        Print function for the tree with optional highlight

        The highlight value will appear green in the final output.

        """
        lines, *_ = self.root._print_aux(highlight)
        for line in lines:
            print(line)
