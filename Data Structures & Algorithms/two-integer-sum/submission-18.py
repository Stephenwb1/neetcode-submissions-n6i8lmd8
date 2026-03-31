class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {} #value : index

        for i, n in enumerate(nums):
            k = target - n
            if k in hashMap:
                return [hashMap[k], i] 
            hashMap[n] = i 