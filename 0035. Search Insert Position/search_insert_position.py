# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/

def searchInsert(nums: List[int], target: int) -> int:
  lo, hi = 0, len(nums) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] > target:
      hi = mid - 1
    elif nums[mid] < target:
      lo = mid + 1
    else:
      return mid

  return lo
