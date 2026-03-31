class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = defaultdict() # value : index

        # [ 1 2 3 4] target = 7
        #k = 7 - 3 = 4
        #hashMap[3] = 2
        #k = 7 - 4 = 3
        #k in hashMap
        #return nums[3] = 2, 3

        for i in range(len(nums)):
            k = target - nums[i]
            if k in hashMap:
                return [hashMap[k], i]
            hashMap[nums[i]] = i
