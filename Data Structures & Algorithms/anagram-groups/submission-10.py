class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #count array for 26 characters count = [0] * 26
        #hashmap of tuple(count) : list of values pairs

        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        
        return list(hashMap.values())