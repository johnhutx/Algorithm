# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
class Solution:
    # Using the divide and mod operations.
    # Time complexity: O(d), where d is the digits of x
    # Space complexity: O(1)
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 0 == 0):
            return False

        reversed_x = 0
        tmp = x
        while tmp > 0:
            reversed_x = reversed_x * 10 + tmp % 10
            tmp = tmp // 10

        return x == reversed_x

    # reverse the given number only up to the middle digit in x and then compare x with the reversedNum.
    # Time complexity: O(d/2), where d is the digits of x
    # Space complexity: O(1)
    def isPalindrome_1(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 0 == 0):
            return False

        reversed_x = 0
        while x > reversed_x:
            reversed_x = reversed_x * 10 + x % 10
            x = x // 10

        return True if (x == reversed_x or x == reversed_x // 10) else False
