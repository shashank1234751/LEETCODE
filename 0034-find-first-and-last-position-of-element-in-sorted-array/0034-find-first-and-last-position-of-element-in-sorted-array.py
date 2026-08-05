class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right=0,len(nums)-1
        mid=0
        while left<=right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                left=mid
                right=mid
                while left > 0 and nums[left - 1] == target:
                    left -= 1
                while right < len(nums) - 1 and nums[right + 1] == target:
                    right += 1

                return [left,right]
            elif nums[mid]<target:
                left = mid + 1
            elif nums[mid]>target:
                right=mid-1
        return [-1,-1]
        