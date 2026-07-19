class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        string=s[:10]
        freq={}
        freq[string]=1
        ans=[]
        for i in range(10,len(s)):
            string+=s[i]
            string=string[1:]
            freq[string]=freq.get(string,0)+1
        for key,items in freq.items():
            if items>1:
                ans.append(key)
        return ans
            
        