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
