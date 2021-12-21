def isPowerOfTwo(n: int) -> bool:
        
    if n < 1:
        return False
        
    return math.log2(n) % 1 == 0