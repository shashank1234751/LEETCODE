class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        def rotate(start,end):
            while start<end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
        rotate(0,n-1)
        rotate(0,k-1)
        rotate(k,n-1)