class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix and postfix
        #[(1 * 2 * 4 * 6), (1 * 4 * 6), (1 * 2 * 6), (1 * 2 * 4 * 1)]

        #array starts as ones so we can multiply them all

        res = [[1] for i in range(len(nums))]
        
        #prefix
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res





