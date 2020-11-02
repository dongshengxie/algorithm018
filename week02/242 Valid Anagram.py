class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t): 
        	return False
        se = set(s)
        if se == set(t):
            for i in se:
                # 直接比较字符元素个数比较字符的个数
                if s.count(i) != t.count(i):
                	return False
            return True
        else:
            return False