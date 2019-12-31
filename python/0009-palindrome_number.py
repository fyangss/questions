from typing import List

class Solution:
  def isPalindrome(self, x: int) -> bool:
    """
      Do it without conversion to string

      First treat all negatives as non-palindromes as negative sign counts

      Build new the reverse number and check if the reverse number is the same
      as the original number, if it is, it's a palindrome

      Build reverse number by dividing by 10 with integer division
      (nothing prevents reverse number from being a string =)

      If I had to do it without any strings, keep track of numbers inserted
      in the loop and use that to multiply the reverse number

      Ex:
        reverse_number = 0
        iter 0:
          reverse_number * 10^0 + x // 10
        iter 1:
          reverse_number * 10^1 + x // 10
        ...
    """
    if x < 0:
      return False
    if x == 0:
      return True

    reverse_number = ''
    x_copy = x
    while x_copy > 0:
      reverse_number += str(x_copy % 10)
      x_copy = x_copy // 10

    return int(reverse_number) == x


# Testing
soln = Solution()
print("Expected false: got " + str(soln.isPalindrome(123)))
print("Expected false: got " + str(soln.isPalindrome(-121)))
print("Expected true: got " + str(soln.isPalindrome(121)))
print("Expected true: got " + str(soln.isPalindrome(1)))
print("Expected true: got " + str(soln.isPalindrome(777777777)))
