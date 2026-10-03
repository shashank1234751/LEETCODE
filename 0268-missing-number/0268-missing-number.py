class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numy=set(nums)
        for n in range(len(nums)+1):
            if n not in numy:
                return n