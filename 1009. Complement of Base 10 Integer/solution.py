import math

def bitwiseComplement1(n: int) -> int:
        
    if n < 2:
        return int(not n)
    
    m = 1
    while m < n:
        m <<= 1
        m += 1
    
    return n ^ m

def bitwiseCompliment2(n: int) -> int:

    return 2**(math.floor(math.log2(n)) + 1) - 1 - n if n > 1 else int(not n)