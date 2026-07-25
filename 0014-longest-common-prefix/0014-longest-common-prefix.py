class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix=strs[0]
        n=len(strs)
        i=0
        
        for word in strs:
            if word==strs[0]:
                continue
            else:
                while not word.startswith(prefix):
                    prefix=prefix[:-1]
        return prefix
    

        
            