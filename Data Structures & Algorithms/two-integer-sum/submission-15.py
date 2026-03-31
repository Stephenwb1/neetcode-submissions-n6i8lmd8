class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #val : index

        for i, n in enumerate(nums):
            k = target - n
            if k in prevMap:
                return [prevMap[k], i]
            prevMap[n] = i
            