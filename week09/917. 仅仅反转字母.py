class Solution(object):
    def reverseOnlyLetters(self, S):
    	res = []
    	j = len(res)-1
    	for i, x in enumerate(S):
    		if x.isalpha():
    			while not S[j].isalpha():
    				j -= 1
    			res.append(S[j])
    			j -=1
    		else:
    			res.append(x)
    	return "".join(res)

class Solution(object):
    def reverseOnlyLetters(self, S):
        letters = [c for c in S if c.isalpha()]
        ans = []
        for c in S:
            if c.isalpha():
                ans.append(letters.pop())
            else:
                ans.append(c)
        return "".join(ans)

