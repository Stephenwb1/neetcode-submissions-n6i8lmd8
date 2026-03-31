class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #hash set
        hashSet = set()

        for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
        return False