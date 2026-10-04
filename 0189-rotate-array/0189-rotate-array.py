class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        positions={}
        n=len(nums)
        for i in range(n):
            pos=(i+k)%n
            positions[pos]=nums[i]
        for i in range(n):
            nums[i]=positions[i]
        
