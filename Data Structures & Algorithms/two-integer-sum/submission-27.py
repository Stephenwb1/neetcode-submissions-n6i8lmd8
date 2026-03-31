class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #dictionary of number : index pairs
        #so that we can locate and return the index

        hashMap = {}

        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashMap:
                return [hashMap[k], i]
            hashMap[nums[i]] = i
