class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        numdict = {} # value, index

        for i, n in enumerate(numbers):
            if target - n in numdict.keys():
                return [numdict[target-n]+1, i+1]
            numdict[n] = i
        
        