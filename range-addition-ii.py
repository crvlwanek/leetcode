# 598. Range Addition II
# https://leetcode.com/problems/range-addition-ii/

def maxCount(m: int, n: int, ops: List[List[int]]) -> int:

  if not ops:
    return m * n

  x, y = zip(*ops)
  return min(x) * min(y)


def maxCount2(m: int, n: int, ops: List[List[int]]) -> int:

  for x, y in ops:
    m = min(m, x)
    n = min(n, y)

  return m * n
