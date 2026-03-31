class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        #array where the index is the count of each value
        #list of lists

        freq = [[] for i in range(len(nums) + 1)]
        #max size of list is len(nums)

        #we'll make a dictionary to keep track of the count of each value

        hashMap = {} #dict of value : occurance pairs

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1 #default value of zero
        
        #now we can fill up the freq array

        for num, count in hashMap.items():
            freq[count].append(num)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
