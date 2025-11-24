from typing import Iterator

# Generator function is a function that returns a generator iterator.
def count_up_to(n: int) -> Iterator[int]:
    i = 1
    while i <= n:
        yield i
        i += 1

# Fibonacci sequence is a sequence of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.
def fibonacci(n: int) -> Iterator[int]:
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a+b

# Generator expression is a lazy way to create a generator
def generator_expression(n: int) -> Iterator[int]:
    return (x**2 for x in range(n))


if __name__ == "__main__":
    fib = fibonacci(10)
    for f in fib:
        print(f)