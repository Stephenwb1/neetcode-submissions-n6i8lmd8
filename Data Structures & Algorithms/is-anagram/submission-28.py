class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # map with key,value of char,count
        # for each of them, and then compare

        s_map, t_map = {}, {}

        for c in s:
            s_map[c] = s_map.get(c,0) + 1
        
        for c in t:
            t_map[c] = t_map.get(c,0) + 1
        
        if s_map == t_map:
            return True
        return False