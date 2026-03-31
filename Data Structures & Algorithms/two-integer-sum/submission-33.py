class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for n in nums - check if target-num is in the dict, if not then add it

        numDict = {}

        for i, n in enumerate(nums):
            if target - n in numDict:
                return [numDict[target-n], i]
            numDict[n] = i
