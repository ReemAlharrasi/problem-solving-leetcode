class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        numstrs=len(strs)
        minlen=len(strs[0])
        for i in range(len(strs)):
            if len(strs[i])<minlen:
                minlen=len(strs[i])
        prefix=""
        for i in range(minlen):
            temp=strs[0][i]
            for j in range(numstrs):
                if strs[j][i]!=temp:
                    return prefix
            prefix+=temp    
        return prefix
