# 91. Decode Ways

def num_decodings(self, s: str) -> int:
  
  def is_nonzero(index):
    return s[index] != '0'

  def is_two_digit_number(index):
      return s[index] == '1' or (s[index] == '2' and s[index + 1] < '7')

  n = len(s)
  output = [0 for _ in range(n + 1)]
  output[n] = 1
  if is_nonzero(n - 1):
      output[n - 1] = 1

  for i in range(n - 2, -1, -1):
      if is_nonzero(i):
          output[i] += output[i + 1]
      if is_two_digit_number(i):
          output[i] += output[i + 2]

  return output[0]
