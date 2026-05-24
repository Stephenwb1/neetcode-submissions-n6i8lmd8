class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #start at position 0
        #i and j that start at 1, len(nums)-1
        #if target < 0 move i, > 0 move j

        res = []
        nums.sort()
        for i, n in enumerate(nums):
            l = i+1
            r = len(nums)-1

            if i > 0 and n == nums[i - 1]:
                continue

            while l < r:
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    r -=1 

                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res
            