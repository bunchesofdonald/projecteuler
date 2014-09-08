#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""

import math
from utils import prime_numbers


def solve(n):
    primes = prime_numbers(int(math.ceil(math.sqrt(n))))
    for prime in reversed(primes):
        if n % prime == 0:
            return prime

if __name__ == '__main__':
    assert solve(13195) == 29
    print solve(600851475143)
