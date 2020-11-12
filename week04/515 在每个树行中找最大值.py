# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        queue = collections.deque()
        result = []
        queue.append(root)
        while queue:
        	size = len(queue)
        	max_level = float('-inf')
        	for i in range(size):
        		node = queue.popleft()
        		if not node:
        			continue
        		max_level = max(max_level, node.val)
        		queue.append(node.left)
        		queue.append(node.right)
        	if max_level != float('-inf'):
        		result.append(max_level)
        return result

# DFS
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        levels = []
        self.dfs(root, levels, 0)
        return [max(l) for l in levels]

    def dfs(self, root, levels, level):
    	if not root:
    		return 
    	if level == len(levels):
    		levels.append([])
    	levels[level].append(root.val)
    	self.dfs(root.left, levels, level+1)
    	self.dfs(root.right, levels, level+1)