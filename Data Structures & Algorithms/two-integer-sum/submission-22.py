class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #we are going to use a hashMap of value : index pairs
        #
        #for n in nums:
        #   k = target - n[i]
        #   if k in hashMap:
        #   

        hashMap = {} #value : index pairs

        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashMap:
                return [hashMap[k], i]
            hashMap[nums[i]] = i