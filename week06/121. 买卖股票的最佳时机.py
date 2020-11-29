class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for _ in xrange(2)] for _ in xrange(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in xrange(1,n):
            # 第i天卖出的最大收益  
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            # 第i天买入的最大收益  
            dp[i][1] = max(dp[i-1][1],-prices[i])
        return dp[-1][0]

