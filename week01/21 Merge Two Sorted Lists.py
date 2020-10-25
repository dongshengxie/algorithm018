# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#方法一 递归
class Solution:
    def mergeTwoLists(self, l1,l2):
        if not l1: 
            return l2  # 终止条件，直到两个链表都空
        if not l2: 
        	return l1

        if l1.val <= l2.val:  # 递归调用
            l1.next = self.mergeTwoLists(l1.next,l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1,l2.next)
            return l2


#方法二 迭代
class Solution(object):
	def mergeTwoLists(self, l1, l2):
		#增加一个冗余的节点，方便后续处理
		p = ListNode(-1)
		head = p
		while l1 and l2:
			if l1.val<=l2.val:
				p.next,l1 = l1,l1.next
			#else时，将p指向l2节点
			else:
				p.next,l2 = l2,l2.next
			p = p.next

		p.next = l1 if l1 else l2
		return head.next





