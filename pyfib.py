#! py -3

"""Module to generate Fibonacci numbers"""

import argparse


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('count', help='Number of Fibonacci numbers to generate', type=int)
    options = parser.parse_args()
    print(list(fib(options.count)))

