def count_halving_steps(n: int) -> int:
    """Return how many times the loop body runs."""
    return n.bit_length() - 1
