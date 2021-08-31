# 153. Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/


    def findMin(self, nums: List[int]) -> int:
        
        breakpoint = nums[0]
        l, r = 0, len(nums) - 1
        
        def search(l: int, r: int) -> int:
            if l >= r:
                return nums[l]
            
            mid = (l + r) // 2
            if nums[mid] >= breakpoint:
                return search(mid+1, r)
            
            return search(l, mid)
        
        return min(search(l, r), breakpoint)
