# 565. Array Nesting
# https://leetcode.com/problems/array-nesting/

from typing import List

def arrayNesting(nums: List[int]) -> int:

  n = len(nums)
  dp = [-1] * n

  def check_index(i: int, _set: set) -> int:
    if dp[i] != -1:
      return dp[i]

    if i in _set:
      return 0

    _set.add(i)
    dp[i] = check_index(nums[i], _set) + 1
    return dp[i]

  max_value = 0
  for i in range(n):
    max_value = max(max_value, check_index(i, set()))

  return max_value


def arrayNesting2(nums: List[int]) -> int:
        
  max_value = 0

  for k in nums:
    curr_value = 0
    while nums[k] != -1:
      curr_value += 1
      nums[k], k = -1, nums[k]

    max_value = max(max_value, curr_value)

  return max_value
