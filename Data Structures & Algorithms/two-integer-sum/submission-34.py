class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #returning indices, so we need a dict
        #value, index pairs since we want to return the index

        res = {}

        for i, n in enumerate(nums):
            if target - n in res:
                return [res[target-n], i]
            res[n] = i