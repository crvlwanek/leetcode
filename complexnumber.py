# 537. Complex Number Multiplication
# https://leetcode.com/problems/complex-number-multiplication/

def complexNumberMultiply(num1: str, num2: str) -> str:

  def to_tuple(num: str) -> tuple[int]:
    real, imaginary = num.split("+")
    return int(real), int(imaginary.split("i")[0])

  def to_string(real: int, imaginary: int) -> str:
    return f"{real}+{imaginary}i"

  a, b = to_tuple(num1)
  c, d = to_tuple(num2)
  real, imaginary = (a*c - b*d), (a*d + b*c)
  return to_string(real, imaginary)
