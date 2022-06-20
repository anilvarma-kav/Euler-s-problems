""":param
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
"""


def is_polindrome(p):
    return str(p) == str(p)[::-1]


def largest_palindromic_number(n1_digits, n2_digits):
    n1_max = 10 ** n1_digits - 1
    n2_max = 10 ** n2_digits - 1
    n1_min = 10 ** (n1_digits - 1) - 1
    n2_min = 10 ** (n2_digits - 1) - 1
    largest_poly = 0
    n1 = 0
    n2 = 0
    for i in range(n1_max, n1_min, -1):
        for j in range(n2_max, n2_min, -1):
            p = i * j
            if is_polindrome(p):
                if p > largest_poly:
                    largest_poly = p
                    n1 = i
                    n2 = j
    return n1, n2, largest_poly

if __name__=='__main__':
    print(largest_palindromic_number(3,3))