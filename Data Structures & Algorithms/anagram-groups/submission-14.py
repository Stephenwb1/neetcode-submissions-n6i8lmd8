class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #we will have hashMap of count : (list of strings) pairs
        #count will be [0] * 26 so we know what letters are in the word
        #words with the same count value will be appended to the end of the list in the hashMap

        hashMap = defaultdict(list)# count, list of strings pairs

        for s in strs:
            count = [0] * 26;
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
            
        return list(hashMap.values())
