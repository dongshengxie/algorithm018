class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l, r = 0, num + 1
        # [l, r)
        while l < r:
            mid = l + (r - l) / 2
            if mid * mid == num:
                return True
            if mid * mid < num:
                l = mid + 1
            else:
                r = mid
        return False