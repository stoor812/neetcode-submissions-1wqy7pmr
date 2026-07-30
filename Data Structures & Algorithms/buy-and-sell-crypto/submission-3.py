class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        maxP = 0

        # SLIDING WINDOW
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
                right += 1

        return maxP
