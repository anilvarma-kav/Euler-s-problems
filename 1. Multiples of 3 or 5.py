""":param


If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

# Linear complexity - O(N)
def is_multiple(nums, val):
    for num in nums:
        if val % num == 0:
            return True
    return False

# Linear complexity - O(N)
def sum_of_all_multiples(nums, limit):
    s = 0
    for i in range(1, limit):
        print(i)
        if is_multiple(nums, i):
            s = s + i
    return s


if __name__ == "__main__":
    print(sum_of_all_multiples([3, 5], 1000))

#     1 line answer
    print(sum(set(list(range(0,1000,3)) + list(range(0,1000,5)))))
