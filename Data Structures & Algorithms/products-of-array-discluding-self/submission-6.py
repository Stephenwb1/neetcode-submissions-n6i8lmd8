class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we have input, prefix, and postfix and we're gonna put it all
        #into the output array
        #input : [1, 2, 3, 4]
        #prefix: [1, 2, 6, 24]
        #postfix:[24, 24, 12, 4]

        output = [0] * len(nums)

        #for prefix, we go through list forward, and backward for postfix

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output