class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make a hashmap of value : index pairs
        #check if k = target - nums[i] is in the dict
        #if so, return hashMap[k], i

        hashMap = {}

        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashMap.keys():
                return [hashMap[k], i]
            hashMap[nums[i]] = i
        return list(hashMap.values())