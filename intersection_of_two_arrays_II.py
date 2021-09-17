# 350. Intersection of Two Arrays II
# https://leetcode.com/problems/intersection-of-two-arrays-ii/

from collections import Counter

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
  count1 = Counter(nums1)

  def is_intersect(num):

    if count1.get(num, 0):
      count1[num] -= 1
      return True

    return False

  return [num for num in nums2 if is_intersect(num)]
