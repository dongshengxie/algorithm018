#方法一 三次反转
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k %= n
        
        def reverse(nums, t, s):
            while t < s:
                nums[t], nums[s] = nums[s], nums[t]
                t += 1
                s -= 1

        reverse(nums, 0, n-1) #先将数组整体翻转
        reverse(nums, 0, k-1) #将数组前k-1个元素进行翻转
        reverse(nums, k, n-1) #将数组从索引k到末尾进行翻转

    #reverse函数操作可替换成下面三句
        #nums[:] = nums[::-1]
        #nums[:k] = nums[:k][::-1]
        #nums[k:] = nums[k:][::-1]



#方法二 环替换，思路可能想不出来
class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        k = k % l
        start = cur = 0 #初始化起始点，当前点
        prev = nums[cur]
        for i in range(l): #换位置次数等于元素个数
            cur = (cur + k) % l #获取换到的位置
            nums[cur], prev = prev, nums[cur] #换位置，原位置的元素用pre暂存

            if cur == start: # 如果回到起始位置，将起始位置更新到下一个位置
                start = cur = (cur + 1) % l
                prev = nums[cur]




# 方法三 暴力K次循环，超时
class Solution:
    def rotate(self, nums, k):
        for i in range(k):
            previous = nums[-1]
            for j in range(len(nums)):
                nums[j], previous = previous, nums[j]
                