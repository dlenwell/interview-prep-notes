## Dynamic programming

Dynamic programming is a way to reduce complexity by keeping track of what
has already been calculated in the following ways;

- Memoization
- Tabulation

### Memoization

Stick to two high level steps.

- Start with a correct recursive solution
  - visualize the problem as a tree
  - implement the tree using recursion
    - define base cases
  - test it

- Then make it efficient
  - add memo object
  - add a base case to return the memo values
  - store return values in the memo object

#### Examples:
- [fibonacci](memoization_fib.py)
- [grid traveler](memoization_grid_traveler.py)
- [can sum](memoization-canSum.py)
- [has sum](memoization-hasSum.py)
- [best sum](memoization_best_sum.py)
- [can construct](memoization-grid-traveler.py)
