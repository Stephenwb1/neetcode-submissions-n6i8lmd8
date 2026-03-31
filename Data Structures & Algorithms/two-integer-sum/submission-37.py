class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for n in nums - check if target - n is in list , if not, add it to list
        # return indices, so make a dict with value,index
        res = {}

        for i, n in enumerate(nums):
            if (target - n) in res:
                return [res[target-n], i]
            res[n] = i