class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_vol=0
        i=0
        j=len(height)-1
        while i<j:
            cur_vol=min(height[i], height[j]) * (j - i)
            if cur_vol>max_vol:
                max_vol=cur_vol

            if height[i]>height[j]:
                j-=1
            else:
                i+=1
        return max_vol

            




        