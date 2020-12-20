class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        strs = s.split()
        strs.reverse()
        return ' '.join(strs)



