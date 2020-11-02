class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for s in strs:
        	key = tuple(sorted(s))
        	#if key not in dic:
        		#dic[key] = [s]
        	#else:
        		#dic[key].append(s)
        	dic[key] = dic.get(key, []) + [s]
        return list(dic.values())

