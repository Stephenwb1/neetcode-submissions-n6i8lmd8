class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #bucket sort
        #we'll have a list of occurance: value pairs
        #the index will be the number of occurances
        #the values in the index will be lists of the numbers with that many occurances

        array = [[] for i in range(len(nums)+1)]

        #we can use a dictionary of value: occurance pairs to map
        hashMap = {}

        for i in range(len(nums)):
            hashMap[nums[i]] = hashMap.get(nums[i], 0) + 1
        #hashmap is now filled with value : occurance # pairs

        for i, j in hashMap.items():
            array[j].append(i)
        
        
        output = []
        for i in range(len(array) - 1, -1, -1):
            for num in array[i]:
                output.append(num)
                if len(output) == k:
                    return output

