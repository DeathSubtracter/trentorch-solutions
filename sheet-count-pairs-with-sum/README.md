# Count Pairs With Sum

Intermediate | dsa-sheet | basics | make-it-fast

Given a list of integers `nums` and an integer `target`, return how many pairs of positions `i < j` have `nums[i] + nums[j] == target`.

Pairs are counted by position, so equal values at different positions count separately.

The starter code checks every pair. Make it fast.

### Examples

**Example 1**

Input:

```python
count_pairs_with_sum([1, 2, 3, 4, 3], 6)
```

Output:

```text
2
```

Positions (1, 3) give 2 + 4 and positions (2, 4) give 3 + 3.

**Example 2**

Input:

```python
count_pairs_with_sum([2, 2, 2], 4)
```

Output:

```text
3
```

All three pairs of positions sum to 4.

### Constraints

- `0 <= len(nums) <= 2 * 10**5`
- `-10**9 <= nums[i], target <= 10**9`
- The answer can exceed `10**10`.
