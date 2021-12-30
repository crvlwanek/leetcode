def twoSum(nums: List[int], target: int) -> List[int]:
    
    seen = {}
    for i, num in enumerate(nums):
        if num in seen:
            return [seen[num], i]
        
        seen[target - num] = i