class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxi=0
        curr=0
        vowel="aeiou"
        for i in range(k):
            if s[i].lower() in vowel:
                curr+=1
        maxi=curr
        for i in range(k,len(s)):
            if s[i].lower() in vowel:
                curr+=1
            if s[i-k] in vowel:
                curr-=1
            maxi=max(maxi,curr)
        return maxi
