def count_doubling_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    return (n-1).bit_length()
