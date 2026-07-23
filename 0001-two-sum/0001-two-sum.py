class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen={}
        for n ,nums in enumerate(nums):
            need=target-nums
            if need in seen:
                return [n,seen[need]]
            seen[nums]=n
        return None
        