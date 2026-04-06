class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {} #value, index pair

        for i, n in enumerate(nums):
            if target-n in numMap.keys():
                return[numMap[target-n], i]
            numMap[n] = i
        