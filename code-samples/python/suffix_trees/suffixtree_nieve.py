"""
Suffix tree data structure is a way of indexing a string like a suffix trie

Below is a suffix tree that can be queried efficiently and has a managable size
However this is not the most efficient way to do this.

"""
import pptree


class Node(object):
    def __init__(self, label, children={}):
        self.label = label  # label on path leading to this node
        self.children = children  # outgoing edges; maps characters to nodes
        self.parent = None


class SuffixTree(object):

    def __init__(self, string):
        """
        Make suffix tree, without suffix links, from s in quadratic time
        and linear space
        """
        string == "{}$".format(string)
        self.string = string
        self.length = len(string)

        self.root = Node(None)
        self.root.children[string[0]] = Node(string)
        #  trie for just longest suf
        # add the rest of the suffixes, from longest to shortest
        for index in range(1, len(string)):
            # start at root; we’ll walk down as far as we can go
            current = self.root

            character_index = index

            while character_index < len(string):
                if string[character_index] in current.children:
                    child = current.children[string[character_index]]
                    label = child.label

                    # Walk along edge until we exhaust edge label or
                    # until we mismatch
                    offset = character_index + 1

                    while (offset - character_index < len(label)):
                        offset += 1

                    if offset - character_index == len(label):
                        current = child  # we exhausted the edge
                        character_index = offset
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = \
                            label[offset - character_index], string[offset]
                        # create “mid”: new node bisecting edge
                        middle = Node(label[:offset - character_index])
                        middle.children[cNew] = Node(string[offset:])
                        # original child becomes mid’s child
                        middle.children[cExist] = child
                        # original child’s label is curtailed
                        child.label = label[offset - character_index:]
                        # mid becomes new child of original parent
                        current.children[string[character_index]] = middle
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    current.children[string[character_index]] = \
                        Node(string[character_index:])

    def follow_path(self, string):
        """ Follow path given by s.  If we fall off tree, return None.  If we
            finish mid-edge, return (node, offset) where 'node' is child and
            'offset' is label offset.  If we finish on a node, return (node,
            None). """
        current = self.root
        index = 0

        while index < len(string):
            character = string[index]
            if character not in current.children:
                return (None, None)  # fell off at a node

            child = current.children[string[index]]
            label = child.label

            next_index = index + 1

            while next_index - index < len(label) and \
                    next_index < len(string) and \
                    string[next_index] == label[next_index - index]:
                next_index += 1

            if (next_index - index) == len(label):
                current = child  # exhausted edge
                index = next_index
            elif next_index == len(string):
                # exhausted query string in middle of edge
                return(child, next_index - index)
            else:
                return(None, None)  # fell off in the middle of the edge

        return (current, None)  # exhausted query string at internal node

    def has(self, string):
        """
        Return true iff s appears as a substring
        """
        node, offset = self.follow_path(string)

        return(node is not None)

    def has_suffix(self, string):
        """
        Return true iff s is a suffix
        """
        node, offset = self.follow_path(string)
        if node is None:
            print("first fail")
            return(False)  # fell off the tree

        if offset is None:
            print("second")
            # finished on top of a node
            return('$' in node.children)
        else:
            print("third")
            # finished at offset 'off' within an edge leading to 'node'
            return(node.label[offset] == '$')


    def traverse(self):
        """
        itarative traverse depth first
        """
        suffixes = set()
        index = 0
        stack = [self.root]
        printable = {}
        parent = None

        printable['0'] = pptree.Node("root")

        while stack:
            current = stack.pop()

            if current.label not in suffixes:
                # do it
                # print('Visiting: ', current.label)

                if current.parent is not None:
                    printable[str(index)] = pptree.Node(
                        "--{} ".format(current.label.zfill(2)),
                        printable[current.parent]
                    )

                suffixes.add(current.label)

                for child in current.children:
                    child_node = current.children[child]
                    child_node.parent = str(index)
                    stack.append(child_node)

                index += 1

        pptree.print_tree(printable['0'], horizontal=True)
        return()

    def printHeap(self):
        """

        """
        nodes = {}

        nodes['0'] = pptree.Node("--{} ".format(str(self.storage[0]).zfill(2)),)

        for index in range(len(self.storage)):

            if self.hasParent(index):
                nodes[str(index)] = pptree.Node(
                    "--{} ".format(str(self.storage[index]).zfill(2)),
                    nodes[str(self.getParentIndex(index))]
                )

        pptree.print_tree(nodes['0'], horizontal=True)

def main():
    string = 'Banana'
    print("string:", string)

    tree = SuffixTree(string)

    print()
    print('tree.has("quick") = {}'.format(tree.has("quick")))
    print()
    print('tree.has_suffix(" dog!") = {}'.format(tree.has_suffix(" dog!")))
    print()
    print("traverse:")
    print(tree.traverse())


if __name__ == "__main__":
    """
    """
    main()
