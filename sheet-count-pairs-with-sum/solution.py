def count_pairs_with_sum(nums, target):
    """Return how many pairs i < j have nums[i] + nums[j] == target."""
    seen = {}
    pairs = 0

    for x in nums:
        pairs += seen.get(target - x, 0)
        seen[x] = seen.get(x, 0) + 1

    return pairs
