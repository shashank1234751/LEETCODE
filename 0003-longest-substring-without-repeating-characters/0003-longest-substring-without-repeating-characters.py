class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string=[]
        maxi=0
        count=0
        for ch in s:
            while ch in string:
                string=string[1:]
            string+=ch
            maxi=max(maxi,len(string))
        return maxi
        
