def largest_n(growth: str, budget: int) -> int:
    """Return the largest n whose cost is at most budget, or 0 if none."""

    def cost(n):
        if growth == "n":
            return n
        elif growth == "n log n":
            return n * (n.bit_length() - 1)
        elif growth == "n^2":
            return n * n
        elif growth == "n^3":
            return n * n * n
        elif growth == "2^n":
            return 2 ** n

    # Binary search implementation:
    low = 0
    high = max(budget, 1)
    best_n = 0

    # Avoid calculating enormous powers of 2:
    if growth == "2^n":
        high = budget.bit_length()
        
    while low <= high:
        mid = (low + high) // 2
        
        if cost(mid) <= budget:
            best_n = mid
            low = mid + 1
        else:
            high = mid - 1

    return best_n
