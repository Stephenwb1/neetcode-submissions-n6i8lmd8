class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #hashmap with value, index pairs so we can easily retrieve the index
        hashMap = {}
        
        for i, n in enumerate(nums):
            twoSum = target - n
            if twoSum in hashMap.keys():
                return[hashMap[twoSum], i]
            else:
                hashMap[n] = i