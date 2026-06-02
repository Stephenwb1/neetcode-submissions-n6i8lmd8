class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #definitely a two pointer solution
        #keep track of lowest and highest with l and r
        #loop while l < r

        l, r = 0, 1

        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        return maxP