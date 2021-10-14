## Inverting Trees

Inverting a binary tree is a common programming task in tech screening
interviews.

###Example ([code](invert.py)):

This example includes two methods for inverting trees. One Recursive and one
is iterative.

Before:

```
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
```
After:
```
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
```
