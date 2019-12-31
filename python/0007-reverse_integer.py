from typing import List

class Solution:
  def reverse(self, x: int) -> int:
    """
    Turn int into a string, reverse the string, cast back to int.

    Treat negatives as a special case, get rid of the sign then reattach
    at the end.
    """
    if x == 0:
      return 0
    sign = int(x / abs(x))
    x_str = str(abs(x))

    # python magic :S in other languages either do char swapping or
    # second string that adds from the back
    x_str = x_str[::-1]
    ans = sign * int(x_str)

    if ans > 2**31-1 or ans < -2**31:
      return 0
    return ans

# Testing
soln = Solution()
print(soln.reverse(321))
print(soln.reverse(-12345))
