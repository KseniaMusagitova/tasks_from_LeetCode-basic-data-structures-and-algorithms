class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        profit = 0
        buy = prices[0]
        for sell in range(len(prices)):
            profit = max(profit, prices[sell] - buy)
            buy = min(buy, prices[sell])
        return profit


sol = Solution()
print(sol.maxProfit([7,6,4,3,1]))

