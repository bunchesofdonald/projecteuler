#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def solve(n):
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


if __name__ == '__main__':
    assert solve(10) == 23
    print solve(1000)
