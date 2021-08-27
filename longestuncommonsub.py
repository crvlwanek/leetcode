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
