class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #array of count = [0] * 26
        #hashmap of the count array : list of strings that have that count

        hashMap = defaultdict(list) #count : list of strings pairs

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] = count[ord(c) - ord("a")] + 1

            hashMap[tuple(count)].append(s)
        
        return list(hashMap.values())
