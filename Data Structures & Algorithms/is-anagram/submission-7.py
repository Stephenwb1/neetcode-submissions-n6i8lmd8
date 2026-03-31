class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #we want to sort the letter as the key and the number of times it appears as the value
        #racecar: r: 2 , a: 2, c: 2, e: 1
        #hash map (dictionary) for this

        

        if len(s) != len(t): #can't be different lengths
            return False
        
        hashMap_s, hashMap_t = {}, {}

        for i in range(len(s)):
            hashMap_s[s[i]] = hashMap_s.get(s[i], 0) + 1
            hashMap_t[t[i]] = hashMap_t.get(t[i], 0) + 1
        if hashMap_s == hashMap_t:
            return True
        return False
