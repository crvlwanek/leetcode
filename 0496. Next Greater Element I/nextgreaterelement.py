# 496. Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/

def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
  stack, indicies = [], {}
  for num in nums2[::-1]:
    while stack and num > stack[-1]:
      stack.pop()
    if stack:
      indicies[num] = stack[-1]
    stack.append(num)

  return [indicies.get(num, -1) for num in nums1]
