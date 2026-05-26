class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #array where the index represents the count and the values are a list of values
        #use a hashmap to get the counts: value, count pairs
        
        hashMap = {}
        array = [[] for i in range(len(nums) + 1)]

        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1
        for n, count in hashMap.items():
            array[count].append(n)

        res = []
        for i in range(len(array) - 1, 0, -1):
            for n in array[i]:
                res.append(n)
                if len(res) == k:
                    return res
        

