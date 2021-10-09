## Quick Sort

This is a classic recursive quick sort method that uses recursion.

### Example: ([code](quicksort.py))

Basically this example uses the last number in the sequence as a pivot point and
sorts items that are less than the pivot in one group and more in another.

Then concats sub calls of the two sides together. in the end you end up
with a sorted list.

####input:
```
.---.---.---.---.
| 4 | 1 | 3 | 2 |
'---'---'---'---'
```

####Basic Flow:

```
      .---.---.---.---.
      | 4 | 1 | 3 | 2 |
      '---'---'---'---'
       /      ^     \
  .---.---.       .---.---.
  | 4 | 1 |       | 3 | 2 |
  '---'---'       '---'---'
    / ^ \           / ^ \
.---.   .---.   .---.   .---.
| 4 |   | 1 |   | 3 |   | 2 |
'---'   '---'   '---'   '---'
    \   /           \    /
    merge           merge
       \             /
    .---.---.   .---.---.
    | 1 | 4 |   | 2 | 3 |
    '---'---'   '---'---'
            \   /
            merge
              v
      .---.---.---.---.
      | 1 | 2 | 3 | 4 |
      '---'---'---'---'

```
