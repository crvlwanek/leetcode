# 485. Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/

def findMaxConsecutiveOnes(nums: List[int]) -> int:
  total = output = 0
  for num in nums:
    if num:
      total += 1
    else:
      output = max(output, total)
      total = 0

  return max(output, total)
