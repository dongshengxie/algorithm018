class Solution(object):
    def minimumTotal(self, triangle):
        if not triangle:
            return 0
        n = len(triangle)
        m = len(triangle[-1])
        # 申请的dp数组为最长列+1
        dp = [0 for _ in xrange(m+1)]
        for i in xrange(n-1,-1,-1):
            # 从左到右的方式计算
            for j in xrange(len(triangle[i])):
                dp[j] = min(dp[j],dp[j+1]) + triangle[i][j]
        # dp数组的第一个元素即为最终结果
        return dp[0]

