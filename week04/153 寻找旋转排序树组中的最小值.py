class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        mid = left
        while nums[left] >= nums[right]:
            if left + 1 == right:
                mid = right
                break
            mid = (left + right) / 2
            if nums[mid] >= nums[left]:
                left = mid
            elif nums[mid] <= nums[right]:
                right = mid
        return nums[mid]