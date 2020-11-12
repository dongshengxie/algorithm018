# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# BFS方法
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        queue.append(root)
        result = []
        while queue:
        	size = len(queue)
        	level = []
        	for _ in range(size):
        		cur = queue.popleft()
        		if not cur:
        			continue
        		level.append(cur.val)
        		queue.append(cur.left)
        		queue.append(cur.right)
        	if level:
        		result.append(level)
        return result


# DFS方法
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.level(root, 0, result)
        return result

    def level(self, root, level, result):
    	if not root:
    		return

    	if len(result) == level:
    		result.append([])
    	result[level].append(root.val)
    	if root.left:
    		self.level(root.left, level +1, result)
    	if root.right:
    		self.level(root.right, level +1, result)
