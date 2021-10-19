# 978. Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/

def maxTurbulenceSize(arr: List[int]) -> int:
  prev_sign = 0
  streak = max_streak = 1
  for i in range(1, len(arr)):
    diff = arr[i] - arr[i - 1]
    curr_sign =  diff // abs(diff) if diff else 0
    if not curr_sign:
      streak = 1
    elif curr_sign == prev_sign:
      streak = 2
    else:
      streak += 1
    max_streak = max(max_streak, streak)
    prev_sign = curr_sign

  return max_streak
