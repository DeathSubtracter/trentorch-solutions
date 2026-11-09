def count_triple_loop(n: int) -> int:
    """Return how many times `count += 1` runs."""
    return n * (n+1) * (n+2) // 6
