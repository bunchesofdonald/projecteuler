import itertools
import unittest


class TestFibonacciGenerator(unittest.TestCase):
    def test_generates_fibonacci_numbers(self):
        """The Fibonacci Generator should be able to generate fibonacci numbers"""
        expected = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ]
        generated = list(itertools.islice(fibonacci_numbers(), 10))
        self.assertEqual(expected, generated)


def fibonacci_numbers():
    x = y = 1
    while True:
        yield y
        y, x = x + y, y


class TestPrimeNumberGenerator(unittest.TestCase):
    def test_generates_prime_numbers(self):
        """The Prime Number generator should be able to generate prime numbers less than a given number"""
        expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, ]
        generated = prime_numbers(30)
        self.assertEqual(expected, generated)


def prime_numbers(n):
    namespace = range(n + 1)
    finish = int(n ** 0.5)

    for i in xrange(2, finish + 1):
        if namespace[i]:
            namespace[2*i::i] = [None] * (n // i-1)

    return [i for i in namespace[2:] if i]
