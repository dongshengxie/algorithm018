class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        reach = 0
        cur = 0
        N = len(nums)
        count = 0
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count