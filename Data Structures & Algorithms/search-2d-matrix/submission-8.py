class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bot = len(matrix) - 1
        
        while top <= bot:
            midRow = (bot + top) // 2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bot = midRow - 1
            else:
                break
        #found the right row

        l, r = 0, len(matrix[0]) - 1
        solRow = (bot + top) // 2

        while l <= r:
            m = (r + l) // 2
            if matrix[solRow][m] < target:
                l = m + 1
            elif matrix[solRow][m] > target:
                r = m - 1
            else:
                return True
        return False
