class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            midway = l + ((r - l) // 2)
            if nums[midway] < target:
                l = midway + 1
            elif nums[midway] >= target:
                r = midway
            else:
                return midway
        return l if (l < len(nums) and nums[l] == target) else -1