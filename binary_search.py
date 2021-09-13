# 704. Binary Search
# https://leetcode.com/problems/binary-search

def search(nums: List[int], target: int) -> int:
  try:
    return nums.index(target)
  except ValueError:
    return -1

def search2(nums: List[int], target: int) -> int:
  lo, hi = 0, len(nums) - 1
  while lo <= hi:
    mid = (lo + hi) // 2
    if nums[mid] > target:
      hi = mid - 1
    elif nums[mid] < target:
      lo = mid + 1
    else:
      return mid

  return -1 
