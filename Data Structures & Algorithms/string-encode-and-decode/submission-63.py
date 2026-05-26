class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:

        l, r = 0, 0
        res = []

        while l < len(s) - 1:
            
            while s[r] and s[r] != '#':
                r += 1
            #r is at #
            print(l, r)
            length = int(s[l:r])
            l = r + 1 
            r = l + length
            print(l, r)
            res.append(s[l:r])
            print(s[l:r])
            l = r 
            r = l
        
        return res


