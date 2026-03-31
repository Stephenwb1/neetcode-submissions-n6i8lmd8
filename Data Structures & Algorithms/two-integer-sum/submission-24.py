class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we have a hashmap of value : index pairs, 
        #and then we check if n is in hashmap

        hashMap = {}

        for i in range(len(nums)):
            k = target - nums[i]

            if k in hashMap:
                return [hashMap[k], i]
            hashMap[nums[i]] = i
        