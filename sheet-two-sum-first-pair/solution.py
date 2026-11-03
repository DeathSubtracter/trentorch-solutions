def two_sum_first_pair(nums, target):
    """Return [i, j] for the first pair of positions that add up to target, or [-1, -1]."""
    seen = {}
    best_pair = [-1, -1]

    for j, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            i = seen[complement]
            
            if best_pair[0] == -1 or i < best_pair[0]:
                best_pair = [i, j]

            # Early exit: in the case that we find a pair with i = 0, since it cannot be smaller than 0.
            if i == 0:
                return best_pair

        if num not in seen:
            seen[num] = j

    return best_pair
