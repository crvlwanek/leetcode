# 764. Largest Plus Sign
# https://leetcode.com/problems/largest-plus-sign/

from typing import List

def orderOfLargestPlusSign(n: int, mines: List[List[int]]) -> int:

  def mines_matrix():
    A = [[1] * n for _ in range(n)]
    for i, j in mines:
      A[i][j] = 0
    return A

  L = mines_matrix()
  for i in range(n):
    for j in range(1, n):
      if not L[i][j]:
        continue
      L[i][j] += L[i][j-1]

  R = mines_matrix()
  for i in range(n):
    for j in range(n - 2, -1, -1):
      if not R[i][j]:
        continue
      R[i][j] += R[i][j+1]

  U = mines_matrix()
  for j in range(n):
    for i in range(n - 2, -1, -1):
      if not U[i][j]:
        continue
      U[i][j] += U[i+1][j]

  D = mines_matrix()
  for j in range(n):
    for i in range(1, n):
      if not D[i][j]:
        continue
      D[i][j] += D[i-1][j]

  return max(min(L[i][j], R[i][j], D[i][j], U[i][j]) for i in range(n) for j in range(n))
