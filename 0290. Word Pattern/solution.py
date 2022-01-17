
def wordPattern(self, pattern: str, s: str) -> bool:
    
    words = s.split()
    if len(pattern) != len(words):
        return False
    
    patternMap = {}
    reserved = set()
    
    for char, word in zip(pattern, words):
        if char not in patternMap:
            if word in reserved:
                return False
            reserved.add(word)
            patternMap[char] = word
            continue
            
        if patternMap[char] != word:
            return False
        
    return True