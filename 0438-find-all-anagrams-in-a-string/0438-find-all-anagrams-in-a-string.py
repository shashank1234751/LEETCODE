class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        target={}
        check={}
        ans=[]
        k=len(p)
        for ch in p:
            target[ch]=target.get(ch,0)+1
        
        for i in range(len(s)):
            if i>=k:
                left=s[i-k]
                check[left]-=1
                if check[left]==0:
                    del check[left]
            check[s[i]]=check.get(s[i],0)+1
            if check==target:
                ans.append(i-k+1)
        return ans

            