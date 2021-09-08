# 848. Shifting Letters
# https://leetcode.com/problems/shifting-letters/

from typing import List

def shiftingLetters(s: str, shifts: List[int]) -> str:

  def shift(char: str, amount: int) -> str:
    return chr((ord(char) - 97 + amount) % 26 + 97)

  for i in range(len(shifts) - 2, -1, -1):
    shifts[i] += shifts[i + 1]

  return "".join(shift(*pair) for pair in zip(s, shifts))
