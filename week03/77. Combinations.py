class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        def recall(n, k, start, result, subset):
            if len(subset) == k:
                result.append(subset[:])
                return
            for i in range(start, n+1):
                subset.append(i)
                recall(n, k, i+1, result, subset)
                subset.pop()
        recall(n, k, 1, result, [])
        return result