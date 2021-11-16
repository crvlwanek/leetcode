# 668. Kth Smallest Number in Multiplication Table
# https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/

def findKthNumber(self, m: int, n: int, k: int) -> int:
    
    def numbersSmallerThan(x):
        return sum(min(x // y, n) for y in range(1, m + 1))
    
    lo, hi = 1, m * n
    while lo < hi:
        mid = (lo + hi)//2
        if numbersSmallerThan(mid) >= k:
            hi = mid
        else:
            lo = mid + 1
            
    return lo