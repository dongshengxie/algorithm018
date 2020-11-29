class Solution:
    def maxProduct(self, nums):
        res = float("-inf")
        imax, imin = 1, 1
        for i in range(len(nums)):
            if nums[i] < 0:
                imax, imin = imin, imax
            imax = max(imax * nums[i], nums[i])
            imin = min(imin * nums[i], nums[i])
            res = max(res, imax)
        return res

# 解题思路
# 一次遍历，遍历过程中更新数值；
# imax为当前值，则最大值为imax = max(imax * nums[i], nums[i])；
# 该题需要注意负号问题，且负号不在一起，会导致最大值变最小值，最小值变最大值；
# 这样需要同时维护imin，遇到负号就交换imax和imin。

