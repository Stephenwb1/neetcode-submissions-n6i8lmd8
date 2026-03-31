class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we will have a count of 26 zeroes [0] * 26
        #hashmap of count : list of strs pairs

        hashMap = defaultdict(list) 

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        return list(hashMap.values())