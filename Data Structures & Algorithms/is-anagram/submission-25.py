class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sDict = {}
        tDict = {}

        for c in s:
            sDict[c] = 1 + sDict.get(c, 0)
            
        for c in t:
            tDict[c] = 1 + tDict.get(c, 0)

        if sDict == tDict:
            return True
        return False