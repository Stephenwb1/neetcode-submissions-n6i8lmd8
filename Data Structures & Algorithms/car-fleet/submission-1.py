class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #pos + speed*n = 10
        # n*speed = 10 - pos
        # n = (10 - pos) / speed
        # n is time !!

        pair = [[p, s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]: #reverse sorted order
            stack.append((target - p) / s) #decimal division
            if len(stack) > 1 and stack[-1] <= stack[-2]: #collision
                stack.pop()
        return len(stack)



