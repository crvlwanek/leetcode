def minStartValue(self, nums: List[int]) -> int:
    
    _min = nums[0]
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
        _min = min(_min, nums[i])
        
    return 1 - _min if _min < 1 else 1