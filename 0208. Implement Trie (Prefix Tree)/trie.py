# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/

class Trie(object):

  def __init__(self):
    self.__trie = {}

  def insert(self, word: str):
    level = self.traverseTree(word, True)
    level["word"] = True

  def search(self, word: str) -> bool:
    level = self.traverseTree(word)
    return level and level.get("word", False)

  def startsWith(self, prefix: str) -> bool:
    level = self.traverseTree(prefix)
    return bool(level)

  def traverseTrie(self, string, insert=False):
    level = self.__trie
    for char in string:
      if not level.get(char, False):
        if insert:
          level[char] = {}
        else:
          return False
      level = level[char]

    return level
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
