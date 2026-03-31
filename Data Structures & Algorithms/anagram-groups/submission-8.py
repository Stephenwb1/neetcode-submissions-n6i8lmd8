class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #we want count[0] * 26 one for each letter
        #we will have a dict of count : lists of strings pairs

        hashMap = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            hashMap[tuple(count)].append(s)
        return (list(hashMap.values()))