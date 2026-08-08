class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=set(nums)
        longest=0
        for n in nums:
            if n-1 not in nums:
                curr=n
                lenght=1
                while curr+1 in nums:
                    curr+=1
                    lenght+=1
                longest=max(longest,lenght)
        return longest