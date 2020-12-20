class Solution(object):
    def reverseWords(self, s):
    	s1 = []
        for word in s.split():
        	s1.append(word[::-1])
        return " ".join(s1)