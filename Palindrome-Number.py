class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        lenx=len(x)
        for i in range(len(x)//2):
            if x[i]!=x[len(x)-1-i]:
                return False
        return True
