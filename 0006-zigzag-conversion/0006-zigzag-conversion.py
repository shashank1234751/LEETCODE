class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows==1 or numRows>len(s):
            return s
        rows=['']*numRows
        idx=0
        for char in s:
            rows[idx]+=char
            if idx==numRows-1:
                val=-1
            elif idx==0:
                val=1
            idx+=val
        return ''.join(rows)
            

        
        
        