""":param
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


#
def SquareSum(n):
    t = (n * (n + 1)) / 2
    return t * t


# SUM = 12 + 22 + 32 + ... + n2 = [n(n+1)(2n+1)] / 6
def SumSquare(n):
    return (n * (n + 1) * (2 * n + 1)) / 6


def SumSquareDiff(n):
    return SquareSum(n) - SumSquare(n)


print(SumSquareDiff(100))
