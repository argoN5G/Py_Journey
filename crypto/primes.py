#!/usr/bin/python3
##
from time import sleep

def naturals(n):
    yield n
    yield from naturals(n+1)


def primes(N):
    n = next(N)
    yield n
    yield from primes(i for i in N if i%n!=0)


s = naturals(0)
while True:
    p = primes(s)
    print("Prime Number: %s"%next(p))
    sleep(0.2)


# recursion issues to be solved
