class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        i = 0

        while i < len(numbers):
            j = i + 1
            while j < len(numbers):
                if target == numbers[i] + numbers[j]:
                    return [i+1, j+1]
                j += 1
            i += 1
        
