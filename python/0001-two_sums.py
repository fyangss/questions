from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      # Go through the input list, for each value calcuate it's other half
      # then store the value inside a map
      #
      # While going through list, check the map to see if that value exists
      #   * If it does, that means it's other half has been seen and they add
      #   up to target. Return current index and stored index since stored
      #   index is where the other number is.
      #   * If it doesn't, store target-cur_number : index into the map so
      #   later values can check against it
      #
      # Can assume unique solution exists
      val_map = {}
      for i in range(len(nums)):
        cur_val = nums[i]
        if cur_val in val_map:
          return [val_map[cur_val], i]
        val_map[target-cur_val] = i

# Testing
soln = Solution()
print(soln.twoSum([2, 7, 11, 15], 22))
