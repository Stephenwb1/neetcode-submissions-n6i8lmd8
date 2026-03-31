class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #defaultdict so we can make it full of lists

        for s in strs:
            count = [0] * 26 #initialize 26 zeroes in an array
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
