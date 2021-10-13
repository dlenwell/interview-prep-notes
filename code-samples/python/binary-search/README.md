## Binary Search

### Search


### Search Binary Tree

In this tree nodes with larger values always sort to the right branch and
lower node values to the left.


                      10  -> root
                    /    \
     left child <- 6      14  -> right child
                  / \     / \
                 5   7  11   16

This contains two objects.. the Tree object and the Node object.

You can create an empty tree like this:
```
tree = Tree()
```

or you can pass in the root node when you create it like this:
```
tree = Tree(Node(5)) <-- makes a new tree with root node with value of 5.
```

then you can just start adding numbers like this:
```
tree.add(value)
```

I've also included a print feature that draws a nice representation of your
