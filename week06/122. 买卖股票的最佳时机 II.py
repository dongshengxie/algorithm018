class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<=1: return 0

        dp = [[None, None] for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])

        return dp[-1][0]    # 返回最后一天且手上没有股票时的获利情况

