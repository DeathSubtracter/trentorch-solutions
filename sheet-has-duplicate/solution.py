def has_duplicate(nums):
    """Return True if any value appears at least twice."""
    seen = set()

    for x in nums:
        if x in seen:
            return True
        else:
            seen.add(x)
    return False
