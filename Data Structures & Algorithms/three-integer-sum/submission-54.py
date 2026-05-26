class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #plan
        #start with the first number
        #l, r are at i+1, len(nums)
        # we sort the list, so then we shift l and r until we find matches

        res = []
        nums.sort()

        for i, n in enumerate(nums):

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < len(nums) - 1 and l < r: #nums[l] for now
                threeSum = n + nums[l] + nums[r]
                if threeSum < 0:
                    l += 1
                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([n, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

        return res

            
