class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 not in nums:
            return len(nums)-1
        zero=0
        left=0
        right=0
        ans=0
        for right in range(len(nums)):
            if nums[right]==0:
                zero+=1
            while zero>1:
                if nums[left]==0:
                    zero-=1
                left+=1
            ans=max(ans,right-left)
        return ans