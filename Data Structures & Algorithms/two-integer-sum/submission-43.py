class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #check if target is in our map, if so return the indices
        numMap = {} #value, index pairs

        for i, n in enumerate(nums):
            k = target - n
            if k in numMap:
                return [numMap[k], i]
            else:
                numMap[n] = i