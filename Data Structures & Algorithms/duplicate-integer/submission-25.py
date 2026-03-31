class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
         hashSet = set()

         for n in range(len(nums)):
            if nums[n] in hashSet:
                return True
            hashSet.add(nums[n])
         return False