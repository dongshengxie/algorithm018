class Solution(object):
    def validPalindrome(self, s):
        isPalindrome = lambda s: s == s[::-1]
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left +1: right +1]) or isPalindrome(s[left:right]) 
        return True