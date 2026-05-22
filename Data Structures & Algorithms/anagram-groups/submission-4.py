from collections import Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        for word in strs:
            # 1. Count letters: Counter("cat") -> {'c':1, 'a':1, 't':1}
            counts = Counter(word)
            
            # 2. Convert to a tuple so it can be a dictionary key
            # sorted(counts.items()) ensures the letters stay in the same order
            key = tuple(sorted(counts.items()))
            
            # 3. Group them safely
            if key not in groups:
                groups[key] = []
            groups[key].append(word)
            
        return list(groups.values())


