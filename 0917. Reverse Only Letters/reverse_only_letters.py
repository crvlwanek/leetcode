# 917. Reverse Only Letters
# https://leetcode.com/problems/reverse-only-letters/

def reverseOnlyLetters(s: str) -> str:
  n = len(s)
  l, r = 0, n - 1
  output = ["" for _ in range(n)]
  while l <= r:
    if not s[l].isalpha():
      output[l] = s[l]
      l += 1
    elif not s[r].isalpha():
      output[r] = s[r]
      r -= 1
    else:
      output[l] = s[r]
      output[r] = s[l]
      l += 1
      r -= 1

  return "".join(output)

def reverseOnlyLetters2(s: str) -> str:
  output = list(s)
  l, r = 0, len(s) - 1
  while l < r:
    if not s[l].isalpha():
      l += 1
    elif not s[r].isalpha():
      r -= 1
    else:
      output[l], output[r] = output[r], output[l]
      l += 1
      r -= 1

  return "".join(output)
