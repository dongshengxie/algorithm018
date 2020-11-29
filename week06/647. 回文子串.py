class Solution(object):
    def countSubstrings(self, s):
        count = 0
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        for l in range(1, N + 1): # step size
            for i in range(N - l + 1):
                j = i + l - 1
                if l == 1 or (l == 2 and s[i] == s[j]) or (l >= 3 and s[i] == s[j] and dp[i + 1][j - 1]):
                    dp[i][j] = True
                    count += 1
        return count