import math

def count_square_loop(n: int) -> int:
    """Return how many times the loop body runs."""
    lo, hi = 1, n
    answer = 0

    while lo <= hi:
        mid = (lo + hi) // 2

        if mid * mid <= n:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer
