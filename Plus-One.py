class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x=len(digits)
        for i in range(x-1,-1,-1):
            if digits[i]==9:
                digits[i]=0
                if i==0:
                    digits.insert(0, 1)
            else:
                digits[i]+=1
                break
        return digits
