class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {} #value : index pairs

        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashMap.keys():
                return [hashMap[k], i]
            hashMap[nums[i]] = i
            