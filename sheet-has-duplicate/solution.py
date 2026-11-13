def has_duplicate(nums):
    """Return True if any value appears at least twice."""
    return len(set(nums)) != len(nums)
