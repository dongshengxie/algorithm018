# 方法一 双指针从前向后比较
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        arr = [0 for _ in range(m + n)]
        i = j = k =0 #初始化

        while j < m or k < n:
            if j == m:
                arr[i] = nums2[k]
                k += 1

            elif k == n:
                arr[i] = nums1[j]
                j += 1

            elif nums1[j] <= nums2[k]:
                arr[i] = nums1[j]
                j += 1

            else:
                arr[i] = nums2[k]
                k += 1
            i += 1

        # 将新数组中的元素再拷贝回去 
        for i in range(len(arr)):
            nums1[i] = arr[i]

#方法二：从后向前
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        i,j,k= m-1, n-1, m+n-1 #初始化坐标

        while i >= 0 or j >= 0:
            # 注意两个边界条件，i<0以及j<0，这表示一个数组已经拷贝完了
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            # 反向比较时，拷贝的是较大的那个元素 
            elif nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1

