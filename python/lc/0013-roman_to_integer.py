from typing import List

class Solution:
  def romanToInt(self, s: str) -> int:
    """
    Build a static map of all the roman -> int values.

    Do a sliding window of 2 while looking at the first value,
    if it's a special case look at the second value and see
    if matches the special case, if it does, add the number
    to sum and move ahead two, otherwise add only first number
    and move ahead one.

    Range 1 - 3999
    """
    output = 0
    i = 0
    while i < len(s):
      first_char = s[i]
      second_char = ''
      if i + 1 < len(s):
        second_char = s[i+1]

      combined = first_char + second_char
      # can also combine two helper functions by making more keys
      # now that I think about it :S
      if self.specialCase(combined):
        output += self.mapRomanToInt(second_char) - self.mapRomanToInt(first_char)
        i += 2
      else:
        output += self.mapRomanToInt(first_char)
        i += 1

    return output

  def mapRomanToInt(self, s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    return roman_map.get(s)

  def specialCase(self, s: str) -> bool:
    cases = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']
    return s in cases


# Testing
soln = Solution()
print("Expecting 2: got " + str(soln.romanToInt('II')))
print("Expecting 4: got " + str(soln.romanToInt('IV')))
print("Expecting 1984: got " + str(soln.romanToInt('MCMLXXXIV')))
