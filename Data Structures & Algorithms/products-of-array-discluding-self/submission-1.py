class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we can do this all in the output array by finding
        #the prefix and postfix multiples
        #example [1, 2, 3, 4]
        #prefix= [1, 2, 6, 24]
        #postfix=[24, 24, 12, 4]
        #but we are going to combine them into the output to get
        #[(1*24), (1*12), (2*4), (6*1)]
        #we are using the prefix of the previous index, and the postfix of
        #the next index and multiplying them 
        #but we're going to do that all at once in the output array
        #first, we'll add in the prefix calculation into the output array
        #then we'll traverse backwards through the array, multiplying in
        #the postfix values

        output = [0] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            #we're gonna additively increase prefix
            output[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output











