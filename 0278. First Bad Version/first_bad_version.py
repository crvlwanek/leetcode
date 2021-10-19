# 278. First Bad Version
# https://leetcode.com/problems/first-bad-version/

def firstBadVersion(n: int) -> int:
  lo, hi = 1, n
  while lo <= hi:
    mid = (lo + hi) // 2
    if isBadVersion(mid):
      hi = mid - 1
    else:
      lo = mid + 1

  return lo
