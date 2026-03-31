class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         #make a set
         #if number in the set, return true , else return false

         hashSet = set()

         for n in nums:
            if n in hashSet:
                return True
            hashSet.add(n)
         return False