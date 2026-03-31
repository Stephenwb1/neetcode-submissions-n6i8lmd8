class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #dictionary of letter : occurance pairs

        d_s, d_t = {}, {}

        #anagrams are the same length

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            d_s[s[i]] = d_s.get(s[i], 0) + 1
            d_t[t[i]] = d_t.get(t[i], 0) + 1
        return d_t == d_s