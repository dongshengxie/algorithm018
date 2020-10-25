class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        i, j = 0, 1      #i，j为前后指针
        while j < len(nums):      #j循环到数组最后一位截止
            if nums[i] != nums[j]: 
                i += 1 
                nums[i] = nums[j]      #不相等将j位置元素赋给i+1, i再后移一位
            else:
                j += 1      #相等则j后移一位

        return i + 1    #i位置为新数组最后一位，长度为i+1

