"""Fibonacci number generator script."""

from typing import Iterator


def fibonacci() -> Iterator[int]:
    """Yield the infinite Fibonacci sequence starting from zero."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def main(limit: int = 10) -> None:
    """Print the first ``limit`` Fibonacci numbers."""
    for index, value in zip(range(limit), fibonacci()):
        print(f"F({index}) = {value}")


if __name__ == "__main__":
    main()
