class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #make a count array [0] * 26
        #we will have a result dict of count : list of words pairs


        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        return list(hashMap.values())