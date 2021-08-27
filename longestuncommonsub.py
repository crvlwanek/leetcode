# 522. Longest Uncommon Subsequence II
# https://leetcode.com/problems/longest-uncommon-subsequence-ii/

def findLUSlength(strs: List[str]) -> int:
  good, rejects = set(), set()
  for s in strs:
    current = set()
    for i in range(1, len(s)+1):
      for comb in itertools.combinations(s, i):
        if comb in rejects:
          continue
        if comb in good:
          good.remove(comb)
          rejects.add(comb)
          continue
        current.add(comb)

    for comb in current:
      good.add(comb)

  if not good:
    return -1
  return max(len(item) for item in good)

def findLUSlength2(strs: List[str]) -> int:

  def isSubsequence(s1: str, s2: str) -> bool:
    s2 = iter(s2)
    return all(char in s2 for char in s1)

  strs.sort(key=len, reverse=True)
  for i, s1 in enumerate(strs):
    if all(not isSubsequence(s1, s2) for j, s2 in enumerate(strs) if i != j):
      return len(s1)

  return -1
