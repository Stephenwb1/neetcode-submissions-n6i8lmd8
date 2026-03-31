class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #two dicts for s and t 
        #dicts will be letter:occurance pairs

        ds, dt = {}, {}

        if len(s) != len(t):
            return False

        #anagrams are the same length

        for i in range(len(s)):
            ds[s[i]] = ds.get(s[i], 0) + 1
            dt[t[i]] = dt.get(t[i], 0) + 1
        return ds == dt