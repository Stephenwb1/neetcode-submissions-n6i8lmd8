class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #homogenous min stack
        #stack contains [index, value]
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI #distance
            stack.append((t, i))
        return res