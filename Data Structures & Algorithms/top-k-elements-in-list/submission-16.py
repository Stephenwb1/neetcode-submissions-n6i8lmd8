class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        #result will be an array with length len(nums) (-1?)
        #index of array will be count, value will be value
        
        hashMap = {} #value : occurance pairs

        result = [[] for i in range(len(nums)+1)]
        #for i, n in hashMap

        for n in nums:
            hashMap[n] = hashMap.get(n, 0) + 1 #increase hashmap by one for each value
        
        for i, n in hashMap.items(): #values, occurances
            result[n].append(i)
        
        output = []
        for i in range(len(result) -1 , -0, -1):
            for num in result[i]:
                output.append(num)
                if len(output) == k:
                    return output
