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


def complexNumberBuiltIn(num1: str, num2: str) -> str:

    def convert(num: str) -> complex:
        r, i = num.split("+")
        return complex(int(r), int(i.split("i")[0]))

    num3 = convert(num1) * convert(num2)
    return f"{num3.real:.0f}+{num3.imag:.0f}i"


def complexNumberReplace(num1: str, num2: str) -> str:
    num3 = complex(num1.replace("+-", "-").replace("i", "j")) * \
        complex(num2.replace("+-", "-").replace("i", "j"))

    return f"{num3.real:.0f}+{num3.imag:.0f}i"
