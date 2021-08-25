# 633. Sum of Square Numbers
# https://leetcode.com/problems/sum-of-square-numbers/

import math

def judgeSquareSum(c: int) -> bool:
  squares = {i**2 for i in range(math.ceil(math.sqrt(c)) + 1)}

  for square in squares:
    if c - square in squares:
      return True

  return False

def judgeSquareComprehension(c: int) -> bool:
  squares = {i**2 for i in range(math.ceil(math.sqrt(c)) + 1)}
  return any(c - sq in squares for sq in squares)
