class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMap = defaultdict(list)

        for s in strs:
            array = [0] * 26 #one column per letter
            for c in s:
                array[ord(c) - ord('a')] += 1
            hashMap[tuple(array)].append(s)
        return list(hashMap.values())