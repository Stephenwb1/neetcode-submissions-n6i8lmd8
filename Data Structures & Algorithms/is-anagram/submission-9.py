class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashMap_s, hashMap_t = {}, {}

        if len(s) != len(t):
            return False
        
        #strings are the same length

        for i in range(len(s)):
            hashMap_s[s[i]] = 1 + hashMap_s.get(s[i], 0)
            hashMap_t[t[i]] = 1 + hashMap_t.get(t[i], 0)
        return hashMap_s == hashMap_t