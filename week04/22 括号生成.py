class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result =[]
        self.dfs(result,n,n,'')
        return result
       
    def dfs(self, result,left, right, path):
    	if left == 0 and right ==0:
    		result.append(path)
    		return
    	if left>0:
    		self.dfs(result, left-1,right,path+'(')
    	if left<right:
    		self.dfs(result,left,right-1,path+')')